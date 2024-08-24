"""Initial migration bookings, hotels and rooms

Revision ID: 5b1e97eb10c9
Revises: 8e22ec16d662
Create Date: 2024-08-24 10:27:31.321054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b1e97eb10c9'
down_revision: Union[str, None] = '8e22ec16d662'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bookings', sa.Column('total_days', sa.Integer(), sa.Computed("DATE_PART('day', date_to - date_from)", ), nullable=True))
    op.add_column('bookings', sa.Column('total_cost', sa.Integer(), sa.Computed('price * total_days', ), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bookings', 'total_cost')
    op.drop_column('bookings', 'total_days')
    # ### end Alembic commands ###
