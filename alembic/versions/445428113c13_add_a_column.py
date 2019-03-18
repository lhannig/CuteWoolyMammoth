"""add a column

Revision ID: 445428113c13
Revises: 9fa3fb1e3212
Create Date: 2019-03-18 15:05:13.477395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '445428113c13'
down_revision = '9fa3fb1e3212'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('yarn', sa.Column('length', sa.Integer))


def downgrade():
    op.drow_column('yarn', 'length')
