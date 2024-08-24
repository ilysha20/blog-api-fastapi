"""Fix table user add email column to users and remove name column

Revision ID: f59c2122955d
Revises: 38f9c3c2cc95
Create Date: 2024-08-24 10:35:08.474754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f59c2122955d'
down_revision: Union[str, None] = '38f9c3c2cc95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.drop_column('users', 'user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
