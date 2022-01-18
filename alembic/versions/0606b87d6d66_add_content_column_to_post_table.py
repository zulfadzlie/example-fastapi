"""add content column to post table

Revision ID: 0606b87d6d66
Revises: 642b3af26060
Create Date: 2022-01-15 12:24:38.108530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0606b87d6d66'
down_revision = '642b3af26060'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )

    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass