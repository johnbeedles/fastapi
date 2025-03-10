"""create posts table

Revision ID: 13127811ec58
Revises: 
Create Date: 2025-03-10 09:05:00.175964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13127811ec58'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('published', sa.Boolean(), server_default="True", nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
