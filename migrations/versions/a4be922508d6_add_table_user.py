"""add table user

Revision ID: a4be922508d6
Revises: 40319193639c
Create Date: 2020-02-17 19:45:34.596081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4be922508d6'
down_revision = '40319193639c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=False),
    sa.Column('authentication_token', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('app_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['app_id'], ['app.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('authentication_token'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
