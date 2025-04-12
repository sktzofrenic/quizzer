"""Todo views."""
import datetime as dt

from flask import request
from flask_restful import Resource, reqparse

from quizzer.api.models import (
    GameMemoryVerse,
    GameMemoryVerseAnswer,
    GameMemoryVerseAnswerWord,
)
from quizzer.extensions import api, pusher_client

parser = reqparse.RequestParser(bundle_errors=True)


class VerseGameApi(Resource):

    def get(self):
        parser.add_argument('verse', location='args')
        parser.add_argument('sendVerse', location='args')
        parser.add_argument('retrieveActiveVerse', location='args')
        parser.add_argument('getAllAvailableVerses', location='args')
        parser.add_argument('answers', location='args')
        parser.add_argument('clearVerses', location='args')
        args = parser.parse_args()
        print(args)

        if args.get('getAllAvailableVerses'):
            verses = GameMemoryVerse.query.order_by(GameMemoryVerse.created_at.desc()).all()
            return {
                'success': True,
                'verses': [verse.serialized for verse in verses]
            }

        if args.get('clearVerses'):
            active_verses = GameMemoryVerse.query.filter(
                (GameMemoryVerse.active == True)
            ).all()
            for verse in active_verses:
                verse.active = False
                verse.save()

            pusher_client.trigger('ssgame-1', 'versesCleared', {})

            return {
                'success': True,
                'message': 'Active verses cleared'
            }

        if args.get('retrieveActiveVerse'):
            verse = GameMemoryVerse.query.filter(
                (GameMemoryVerse.active == True)
            ).first()
            return {
                'success': True,
                'verse': verse.serialized if verse else None
            }

        if args.get('sendVerse'):
            verse = GameMemoryVerse.query.filter(
                (GameMemoryVerse.id == args['sendVerse'])
            ).first()

            verse.active = True
            verse.save()

            pusher_client.trigger('ssgame-1', 'memoryVerse', {
                'verse': verse.serialized
            })

            return {
                'success': True,
                'verse': verse.serialized
            }

        if args.get('answers'):
            answers = GameMemoryVerseAnswer.query.filter(
                (GameMemoryVerseAnswer.created_at >= dt.datetime.now() - dt.timedelta(days=1)) &
                (GameMemoryVerseAnswer.game_memory_verse_id == args['answers'])
            ).all()
            return {
                'success': True,
                'answers': [answer.serialized for answer in answers]
            }

        if args.get('verse'):
            verse = GameMemoryVerse.query.filter(GameMemoryVerse.id == args['verse']).first()
            return {
                'success': True,
                'verse': verse.serialized
            }


    def post(self):
        parser.add_argument('answer', location='args')
        args = parser.parse_args()
        print(args)

        json_data = request.get_json(force=True)
        print('\n\nPOSTED DATA', json_data)

        if not json_data:
            return {
                'success': False,
                'message': 'No data provided'
            }

        if args.get('answer'):
            answer = GameMemoryVerseAnswer.query.filter(
                (GameMemoryVerseAnswer.game_memory_verse_id == json_data['verseId']) &
                (GameMemoryVerseAnswer.name == json_data['name']) &
                (GameMemoryVerseAnswer.created_at >= dt.datetime.now() - dt.timedelta(days=1))
            ).first()
            if not answer:
                answer = GameMemoryVerseAnswer.create(name=json_data['name'],
                                                      game_memory_verse_id=json_data['verseId'])
                answer.save()

            answer.game_memory_verse_answer_words = []

            for index, word in enumerate(json_data['words']):
                word = GameMemoryVerseAnswerWord.create(
                    word=word,
                    game_memory_verse_answer_id=answer.id,
                    position=index+1
                )

            answer.get_score()

            pusher_client.trigger('ssgame-1', 'memoryVerseAnswer', {
                'answer': answer.serialized
            })
            print(answer.score, 'hello??')

            return {
                'success': True,
                'message': 'Answer received',
                'score': float(answer.score)
            }

        return {
            'success': True,
        }


    def put(self):
        return {
            'success': True
        }

    def delete(self):
        parser.add_argument('ids', location='args')
        args = parser.parse_args()
        print(args)



api.add_resource(VerseGameApi,
                 '/game-verses')


