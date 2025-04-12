"""empty message

Revision ID: 1c96861c6216
Revises: 
Create Date: 2025-04-12 10:04:46.440979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c96861c6216'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_memory_verses',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('reference', sa.Text(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_memory_verse_answers',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('game_memory_verse_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('score', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('exact_correct_words', sa.Integer(), nullable=True),
    sa.Column('close_correct_words', sa.Integer(), nullable=True),
    sa.Column('incorrect_words', sa.Integer(), nullable=True),
    sa.Column('missed_words', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_memory_verse_id'], ['game_memory_verses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_memory_verse_bank_words',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('game_memory_verse_id', sa.Integer(), nullable=True),
    sa.Column('word', sa.Text(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_memory_verse_id'], ['game_memory_verses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_memory_verse_words',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('game_memory_verse_id', sa.Integer(), nullable=True),
    sa.Column('word', sa.Text(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_memory_verse_id'], ['game_memory_verses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_memory_verse_answer_words',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('game_memory_verse_answer_id', sa.Integer(), nullable=True),
    sa.Column('word', sa.Text(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_memory_verse_answer_id'], ['game_memory_verse_answers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_memory_verse_answer_words')
    op.drop_table('game_memory_verse_words')
    op.drop_table('game_memory_verse_bank_words')
    op.drop_table('game_memory_verse_answers')
    op.drop_table('game_memory_verses')
    # ### end Alembic commands ###
