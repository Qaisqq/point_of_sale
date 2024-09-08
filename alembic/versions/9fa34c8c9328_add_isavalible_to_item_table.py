"""Add isAvalible to item table

Revision ID: 9fa34c8c9328
Revises: fb644855b0a3
Create Date: 2024-09-08 09:20:46.227323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fa34c8c9328'
down_revision: Union[str, None] = 'fb644855b0a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('items', sa.Column('isAvailable', sa.Boolean(), nullable=True))

def downgrade() -> None:
    op.drop__column('items', sa.Column('isAvailable', sa.Boolean(), nullable=True))