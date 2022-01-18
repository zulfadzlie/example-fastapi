"""create posts table

Revision ID: 642b3af26060
Revises: 
Create Date: 2022-01-15 07:30:46.709553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642b3af26060'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )  
    pass


def downgrade():
    op.drop_table('posts')
    pass
