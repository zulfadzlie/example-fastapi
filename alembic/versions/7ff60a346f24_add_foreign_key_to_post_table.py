"""add foreign key to post table

Revision ID: 7ff60a346f24
Revises: e4a3d4a7d3fc
Create Date: 2022-01-15 15:42:38.631673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ff60a346f24'
down_revision = 'e4a3d4a7d3fc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column(
            'owner_id', sa.Integer(),
            nullable=False
        )
    )

    op.create_foreign_key(
        'post_users_fk',
        source_table="posts",
        referent_table="users",
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )

    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')

    pass