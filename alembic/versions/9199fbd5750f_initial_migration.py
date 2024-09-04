"""Initial migration

Revision ID: 9199fbd5750f
Revises: 
Create Date: 2024-09-04 10:49:23.290138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9199fbd5750f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('category_id', sa.Integer(), nullable=False, primary_key=True, index=True, unique=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('img_url', sa.String(), nullable=True)
    )

    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), primary_key=True, index=True, nullable=False),
        sa.Column('name', sa.String(), unique=True, nullable=False),
        sa.Column('pcs', sa.Integer(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('weight', sa.Integer(), nullable=True),
        sa.Column('unit_cost', sa.Integer(), nullable=True),
        sa.Column('sale', sa.BOOLEAN(), nullable=True),
        sa.Column('alias', sa.String(), nullable=True),
        sa.Column('printer', sa.String(), nullable=True),
        sa.Column('img_url', sa.String(), nullable=True),
        sa.Column('category_id', sa.Integer(), sa.ForeignKey('categories.category_id', ondelete='SET NULL'), nullable=True)
    )

    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False, index=True, unique=True),
        sa.Column('status', sa.String(), nullable=True, default='Open'),
        sa.Column('delievered_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.Column('takeout', sa.Boolean(), nullable=True),
        sa.Column('table_id', sa.Integer(), nullable=True),
        sa.Column('discount', sa.Boolean(), nullable=True),
        sa.Column('amount_before_discount', sa.Integer(), nullable=True),
        sa.Column('amount_after_discount', sa.Integer(), nullable=True)
    )

    op.create_table(
        'order_items',
        sa.Column('order_id', sa.Integer(), sa.ForeignKey('orders.id'), primary_key=True),
        sa.Column('item_id', sa.Integer(), sa.ForeignKey('items.id'), primary_key=True),
        sa.Column('item_quantity', sa.Integer(), default=1)
    )

def downgrade() -> None:
    op.drop_table('order_items')
    op.drop_table('orders')
    op.drop_table('items')
    op.drop_table('categories')
