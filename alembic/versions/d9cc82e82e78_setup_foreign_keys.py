"""setup foreign keys

Revision ID: d9cc82e82e78
Revises: 58cd20e2ff94
Create Date: 2025-03-10 09:27:57.365919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9cc82e82e78'
down_revision: Union[str, None] = '58cd20e2ff94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key('fk_posts_owner_id', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('fk_votes_post_id', 'votes', 'posts', ['post_id'], ['id'])
    op.create_foreign_key('fk_votes_user_id', 'votes', 'users', ['user_id'], ['id'])
    pass


def downgrade() -> None:
    op.drop_constraint('fk_votes_user_id', 'votes', type_='foreignkey')
    op.drop_constraint('fk_votes_post_id', 'votes', type_='foreignkey')
    op.drop_constraint('fk_posts_owner_id', 'posts', type_='foreignkey')
    pass
