"""create tables

Revision ID: a48104e95d11
Revises: 
Create Date: 2022-04-26 23:05:31.188867

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a48104e95d11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(length=128), nullable=False),
                    sa.Column('last_name', sa.String(length=128), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('email',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=256), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('phone',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('number', sa.String(length=256), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    pass
