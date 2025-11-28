# -*- coding: utf-8 -*-
"""Poll models."""
from quizzer.database import Column, Model, SurrogatePK, db, relationship
from quizzer.utils import serialize_object
import datetime as dt
from sqlalchemy.orm import backref


class Poll(SurrogatePK, Model):

    __tablename__ = 'polls'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    question = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)
    allow_multiple_answers = db.Column(db.Boolean, default=False)
    ends_at = db.Column(db.DateTime)

    @property
    def serialized(self):
        return serialize_object(self, self.__class__,
                                answers=[answer.serialized for answer in self.poll_answers])

    @property
    def total_votes(self):
        return sum(len(answer.poll_answer_votes) for answer in self.poll_answers)

    def __repr__(self):
        return '<Poll {}>'.format(self.id)


class PollAnswer(SurrogatePK, Model):

    __tablename__ = 'poll_answers'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'), nullable=False)
    poll = relationship('Poll', backref=backref('poll_answers', order_by='PollAnswer.position.asc()'))
    text = db.Column(db.Text, nullable=False)
    position = db.Column(db.Integer, default=0)

    @property
    def votes_count(self):
        return len(self.poll_answer_votes)

    @property
    def serialized(self):
        return serialize_object(self, self.__class__, votes_count=self.votes_count)

    def __repr__(self):
        return '<PollAnswer {}>'.format(self.id)


class PollAnswerVote(SurrogatePK, Model):

    __tablename__ = 'poll_answer_votes'
    created_at = Column(db.DateTime, default=dt.datetime.now)
    updated_at = Column(db.DateTime, onupdate=dt.datetime.now)
    poll_answer_id = db.Column(db.Integer, db.ForeignKey('poll_answers.id'), nullable=False)
    poll_answer = relationship('PollAnswer', backref='poll_answer_votes')
    voter_identifier = db.Column(db.String(255))

    @property
    def serialized(self):
        return serialize_object(self, self.__class__)

    def __repr__(self):
        return '<PollAnswerVote {}>'.format(self.id)
