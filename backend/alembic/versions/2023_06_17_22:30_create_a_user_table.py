"""Create a user table

Revision ID: 6570abe6aac0
Revises: 
Create Date: 2023-06-17 22:30:21.198513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6570abe6aac0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=70), nullable=False),
    sa.Column('email', sa.String(length=140), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
