# -*- coding: utf-8 -*-
"""Polls API."""
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
        fingerprint = json_data.get('fingerprint')

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

        # Check for existing vote by fingerprint first (more reliable)
        if fingerprint:
            existing_vote = PollAnswerVote.query.join(PollAnswer).filter(
                (PollAnswer.poll_id == poll_id) &
                (PollAnswerVote.fingerprint == fingerprint)
            ).first()

            if existing_vote:
                return {
                    'success': False,
                    'message': 'Already voted on this poll'
                }, 400

        # Fall back to voter_identifier check
        if voter_identifier:
            existing_vote = PollAnswerVote.query.join(PollAnswer).filter(
                (PollAnswer.poll_id == poll_id) &
                (PollAnswerVote.voter_identifier == voter_identifier)
            ).first()

            if existing_vote:
                return {
                    'success': False,
                    'message': 'Already voted on this poll'
                }, 400

        vote = PollAnswerVote.create(
            poll_answer_id=answer_id,
            voter_identifier=voter_identifier,
            fingerprint=fingerprint
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


api.add_resource(PollsApi,
                 '/polls',
                 '/polls/<int:poll_id>')

api.add_resource(PollsAdminApi,
                 '/polls/admin',
                 '/polls/admin/<int:poll_id>')
