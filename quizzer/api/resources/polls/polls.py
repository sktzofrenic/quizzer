# -*- coding: utf-8 -*-
"""Polls API."""
from datetime import datetime, timezone

from flask import request
from flask_restful import Resource, reqparse

from quizzer.api.models import Poll, PollAnswer, PollAnswerVote
from quizzer.extensions import api, db

parser = reqparse.RequestParser(bundle_errors=True)


class PollsApi(Resource):

    def get(self, poll_id=None):
        if poll_id:
            poll = Poll.query.filter(Poll.id == poll_id).first()
            if not poll:
                return {
                    'success': False,
                    'message': 'Poll not found'
                }, 404
            return {
                'success': True,
                'poll': poll.serialized
            }

        polls = Poll.query.filter(Poll.active == True).order_by(Poll.created_at.desc()).all()
        return {
            'success': True,
            'polls': [poll.serialized for poll in polls]
        }

    def post(self, poll_id=None):
        if not poll_id:
            return {
                'success': False,
                'message': 'Poll ID required'
            }, 400

        json_data = request.get_json(force=True)
        if not json_data:
            return {
                'success': False,
                'message': 'No data provided'
            }, 400

        answer_id = json_data.get('answer_id')
        voter_identifier = json_data.get('voter_identifier')

        if not answer_id:
            return {
                'success': False,
                'message': 'Answer ID required'
            }, 400

        poll = Poll.query.filter(Poll.id == poll_id).first()
        if not poll:
            return {
                'success': False,
                'message': 'Poll not found'
            }, 404

        if not poll.active:
            return {
                'success': False,
                'message': 'Poll is closed'
            }, 400

        answer = PollAnswer.query.filter(
            (PollAnswer.id == answer_id) &
            (PollAnswer.poll_id == poll_id)
        ).first()

        if not answer:
            return {
                'success': False,
                'message': 'Answer not found'
            }, 404

        ip_address = request.remote_addr

        # Block exact same voter from voting twice
        if voter_identifier:
            existing_vote = PollAnswerVote.query.join(PollAnswer).filter(
                (PollAnswer.poll_id == poll_id) &
                (PollAnswerVote.voter_identifier == voter_identifier)
            ).first()

            if existing_vote:
                return {
                    'success': False,
                    'message': 'You have already voted on this poll',
                    'already_voted': True,
                    'poll': poll.serialized
                }, 400

        # Rate-limit new voters from the same IP with exponential backoff
        if ip_address:
            previous_votes = PollAnswerVote.query.join(PollAnswer).filter(
                (PollAnswer.poll_id == poll_id) &
                (PollAnswerVote.ip_address == ip_address)
            ).order_by(PollAnswerVote.created_at.desc()).all()

            vote_count = len(previous_votes)
            if vote_count > 0:
                last_vote = previous_votes[0]
                required_wait = 30 * (2 ** (vote_count - 1))
                now = datetime.now(timezone.utc)
                last_vote_time = last_vote.created_at.replace(tzinfo=timezone.utc)
                elapsed = (now - last_vote_time).total_seconds()
                remaining = required_wait - elapsed

                if remaining > 0:
                    retry_after = int(remaining) + 1
                    if retry_after >= 60:
                        minutes = retry_after // 60
                        seconds = retry_after % 60
                        wait_str = f"{minutes}m {seconds}s" if seconds else f"{minutes}m"
                    else:
                        wait_str = f"{retry_after}s"

                    return {
                        'success': False,
                        'message': f'Please wait {wait_str} before voting again',
                        'retry_after': retry_after,
                        'poll': poll.serialized
                    }, 429

        vote = PollAnswerVote.create(
            poll_answer_id=answer_id,
            voter_identifier=voter_identifier,
            ip_address=ip_address
        )
        vote.save()

        poll = Poll.query.filter(Poll.id == poll_id).first()

        return {
            'success': True,
            'message': 'Vote recorded',
            'poll': poll.serialized
        }


class PollsAdminApi(Resource):

    def get(self, poll_id=None):
        if poll_id:
            poll = Poll.query.filter(Poll.id == poll_id).first()
            if not poll:
                return {'success': False, 'message': 'Poll not found'}, 404
            return {'success': True, 'poll': poll.serialized}

        # Return all polls for admin (including inactive)
        polls = Poll.query.order_by(Poll.created_at.desc()).all()
        return {
            'success': True,
            'polls': [poll.serialized for poll in polls]
        }

    def post(self, poll_id=None):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'success': False, 'message': 'No data provided'}, 400

        question = json_data.get('question')
        if not question:
            return {'success': False, 'message': 'Question is required'}, 400

        poll = Poll.create(
            question=question,
            description=json_data.get('description'),
            active=json_data.get('active', True),
            allow_multiple_answers=json_data.get('allow_multiple_answers', False)
        )
        poll.save()

        # Create answers
        answers = json_data.get('answers', [])
        for idx, answer_data in enumerate(answers):
            if isinstance(answer_data, str):
                answer_text = answer_data
            else:
                answer_text = answer_data.get('text', '')

            if answer_text:
                answer = PollAnswer.create(
                    poll_id=poll.id,
                    text=answer_text,
                    position=idx
                )
                answer.save()

        poll = Poll.query.filter(Poll.id == poll.id).first()
        return {
            'success': True,
            'message': 'Poll created',
            'poll': poll.serialized
        }

    def put(self, poll_id=None):
        if not poll_id:
            return {'success': False, 'message': 'Poll ID required'}, 400

        poll = Poll.query.filter(Poll.id == poll_id).first()
        if not poll:
            return {'success': False, 'message': 'Poll not found'}, 404

        json_data = request.get_json(force=True)
        if not json_data:
            return {'success': False, 'message': 'No data provided'}, 400

        if 'question' in json_data:
            poll.question = json_data['question']
        if 'description' in json_data:
            poll.description = json_data['description']
        if 'active' in json_data:
            poll.active = json_data['active']
        if 'allow_multiple_answers' in json_data:
            poll.allow_multiple_answers = json_data['allow_multiple_answers']

        poll.save()

        # Update answers if provided
        if 'answers' in json_data:
            # Delete existing answers and their votes
            for answer in poll.poll_answers:
                PollAnswerVote.query.filter(PollAnswerVote.poll_answer_id == answer.id).delete()
                db.session.delete(answer)
            db.session.commit()

            # Create new answers
            for idx, answer_data in enumerate(json_data['answers']):
                if isinstance(answer_data, str):
                    answer_text = answer_data
                else:
                    answer_text = answer_data.get('text', '')

                if answer_text:
                    answer = PollAnswer.create(
                        poll_id=poll.id,
                        text=answer_text,
                        position=idx
                    )
                    answer.save()

        poll = Poll.query.filter(Poll.id == poll.id).first()
        return {
            'success': True,
            'message': 'Poll updated',
            'poll': poll.serialized
        }

    def delete(self, poll_id=None):
        if not poll_id:
            return {'success': False, 'message': 'Poll ID required'}, 400

        poll = Poll.query.filter(Poll.id == poll_id).first()
        if not poll:
            return {'success': False, 'message': 'Poll not found'}, 404

        # Delete votes and answers
        for answer in poll.poll_answers:
            PollAnswerVote.query.filter(PollAnswerVote.poll_answer_id == answer.id).delete()
            db.session.delete(answer)

        db.session.delete(poll)
        db.session.commit()

        return {
            'success': True,
            'message': 'Poll deleted'
        }


class PollClearVotesApi(Resource):

    def post(self, poll_id=None):
        if not poll_id:
            return {'success': False, 'message': 'Poll ID required'}, 400

        poll = Poll.query.filter(Poll.id == poll_id).first()
        if not poll:
            return {'success': False, 'message': 'Poll not found'}, 404

        # Delete all votes for this poll's answers
        for answer in poll.poll_answers:
            PollAnswerVote.query.filter(PollAnswerVote.poll_answer_id == answer.id).delete()

        db.session.commit()

        # Refresh poll to get updated vote counts
        poll = Poll.query.filter(Poll.id == poll_id).first()

        return {
            'success': True,
            'message': 'All votes cleared',
            'poll': poll.serialized
        }


api.add_resource(PollsApi,
                 '/polls',
                 '/polls/<int:poll_id>')

api.add_resource(PollsAdminApi,
                 '/polls/admin',
                 '/polls/admin/<int:poll_id>')

api.add_resource(PollClearVotesApi,
                 '/polls/<int:poll_id>/clear-votes')
