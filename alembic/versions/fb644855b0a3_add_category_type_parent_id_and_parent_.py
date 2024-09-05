"""Add category_type, parent_id, and parent_name to Category model

Revision ID: fb644855b0a3
Revises: 9199fbd5750f
Create Date: 2024-09-05 11:46:34.844518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb644855b0a3'
down_revision: Union[str, None] = '9199fbd5750f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Manually add new columns to the categories table
    op.add_column('categories', sa.Column('category_type', sa.String(), nullable=True))
    op.add_column('categories', sa.Column('parent_id', sa.Integer(), nullable=True, server_default=None))
    op.add_column('categories', sa.Column('parent_name', sa.String(), nullable=True, server_default=None))


def downgrade():
    # Manually define the reverse operation to remove the columns
    op.drop_column('categories', 'parent_name')
    op.drop_column('categories', 'parent_id')
    op.drop_column('categories', 'category_type')