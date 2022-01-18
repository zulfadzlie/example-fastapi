"""add add last few columbs to post table

Revision ID: 176bf2d0516b
Revises: 7ff60a346f24
Create Date: 2022-01-16 08:58:24.226219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '176bf2d0516b'
down_revision = '7ff60a346f24'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column(
            'published',
            sa.Boolean(), nullable=False, server_default='TRUE'
        )
    )

    op.add_column(
        'posts',
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
        )
    
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
    pass
