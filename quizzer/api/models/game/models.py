# -*- coding: utf-8 -*-
"""User models."""
from quizzer.database import Column, Model, SurrogatePK, db, relationship
from quizzer.utils import serialize_object
import datetime as dt
from sqlalchemy.orm import backref


class GameMemoryVerse(SurrogatePK, Model):

    __tablename__ = 'game_memory_verses'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    reference = db.Column(db.Text)
    text = db.Column(db.Text)
    active = db.Column(db.Boolean, default=False)

    @property
    def serialized(self):
        return serialize_object(self, self.__class__,
                                bank_words=[bank_word.serialized for bank_word in self.game_memory_verse_bank_words],
                                words=[word.serialized for word in self.game_memory_verse_words])

    def __repr__(self):
        return '<GameMemoryVerse {}>' .format(self.id)

class GameMemoryVerseBankWord(SurrogatePK, Model):

    __tablename__ = 'game_memory_verse_bank_words'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    game_memory_verse_id = db.Column(db.Integer, db.ForeignKey('game_memory_verses.id'))
    game_memory_verse = relationship('GameMemoryVerse', backref='game_memory_verse_bank_words')
    word = db.Column(db.Text)

    @property
    def serialized(self):
        return {
            'id': self.id,
            'word': self.word
        }

    def __repr__(self):
        return '<GameMemoryVerseBankWord {}>' .format(self.id)

class GameMemoryVerseWord(SurrogatePK, Model):

    __tablename__ = 'game_memory_verse_words'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    game_memory_verse_id = db.Column(db.Integer, db.ForeignKey('game_memory_verses.id'))
    game_memory_verse = relationship('GameMemoryVerse', 
                                     backref=backref('game_memory_verse_words',
                                                     order_by='GameMemoryVerseWord.position.asc()'
                                                     )
                                     )
    word = db.Column(db.Text)
    position = db.Column(db.Integer)

    @property
    def serialized(self):
        return serialize_object(self, self.__class__)

    def __repr__(self):
        return '<GameMemoryVerse {}>' .format(self.id)

class GameMemoryVerseAnswer(SurrogatePK, Model):

    __tablename__ = 'game_memory_verse_answers'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    game_memory_verse_id = db.Column(db.Integer, db.ForeignKey('game_memory_verses.id'), nullable=False)
    game_memory_verse = relationship('GameMemoryVerse', backref='game_memory_verse_answers')
    name = db.Column(db.Text)
    score = db.Column(db.Numeric(8, 2))
    exact_correct_words = db.Column(db.Integer)
    close_correct_words = db.Column(db.Integer)
    incorrect_words = db.Column(db.Integer)
    missed_words = db.Column(db.Integer)

    def get_score(self):
        positions_used = []
        close_positions_used = []
        correct_words = self.game_memory_verse.game_memory_verse_words
        answer_words = self.game_memory_verse_answer_words
        print([word.word for word in correct_words])
        print([word.word for word in answer_words])

        for correct_word in correct_words:
            for answer_word in answer_words:
                if answer_word.word == correct_word.word and \
                    answer_word.position == correct_word.position and \
                    correct_word.position not in positions_used:

                    positions_used.append(correct_word.position)
                    answer_words.remove(answer_word)
                    break

        for correct_word in correct_words:
            for answer_word in answer_words:
                if answer_word.word == correct_word.word and \
                    correct_word.position not in positions_used:

                    close_positions_used.append(abs(correct_word.position - answer_word.position))
                    answer_words.remove(answer_word)
                    break

        self.exact_correct_words = len(positions_used)
        self.close_correct_words = len(close_positions_used)
        self.worst_outcome = ((len(correct_words) - 1) + len(correct_words)) / 2 * len(correct_words)
        self.multiplied_close_correct_words = 1 - (sum(close_positions_used) / self.worst_outcome)
        self.incorrect_words = len(answer_words)
        self.missed_words = abs(len(correct_words) - (self.exact_correct_words + self.close_correct_words + self.incorrect_words))

        self.score = (self.exact_correct_words + (self.close_correct_words * self.multiplied_close_correct_words)) / len(correct_words) * 100
        self.score -= self.incorrect_words * 10
        if self.score < 0:
            self.score = 0
        self.score = self.score * 10
        self.save()
        return self.score

    @property
    def serialized(self):
        return serialize_object(self, self.__class__)

    def __repr__(self):
        return '<GameMemoryVerseAnswer {}>' .format(self.id)

class GameMemoryVerseAnswerWord(SurrogatePK, Model):

    __tablename__ = 'game_memory_verse_answer_words'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    game_memory_verse_answer_id = db.Column(db.Integer, db.ForeignKey('game_memory_verse_answers.id'))
    game_memory_verse_answer = relationship('GameMemoryVerseAnswer', 
                                     backref=backref('game_memory_verse_answer_words',
                                                     order_by='GameMemoryVerseAnswerWord.position.asc()'
                                                     )
                                     )
    word = db.Column(db.Text)
    position = db.Column(db.Integer)

