"""empty message

Revision ID: 56a677e5b7db
Revises: 
Create Date: 2019-10-30 13:01:21.523208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56a677e5b7db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content_creators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('testbank',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    op.drop_table('students')
    op.drop_table('testbank')
    op.drop_table('courses')
    op.drop_table('content_creators')
    # ### end Alembic commands ###
