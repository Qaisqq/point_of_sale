"""Added variation, price columns to OrderItems

Revision ID: a0d9fc4f85d2
Revises: 9fa34c8c9328
Create Date: 2024-09-08 09:50:15.844249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0d9fc4f85d2'
down_revision: Union[str, None] = '9fa34c8c9328'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('order_items', sa.Column('comment', sa.String(), nullable=True))
    op.add_column('order_items', sa.Column('variation', sa.String(), nullable=True))
    op.add_column('order_items', sa.Column('price', sa.Integer(), nullable=True))



def downgrade() -> None:
    op.drop_column('order_items', sa.Column('comment', sa.String(), nullable=True))
    op.drop_column('order_items', sa.Column('variation', sa.String(), nullable=True))
    op.drop_column('order_items', sa.Column('price', sa.Integer(), nullable=True))

