"""change table name

Revision ID: a4663e0c0d4b
Revises: 287380a40abd
Create Date: 2019-03-19 17:11:21.807624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4663e0c0d4b'
down_revision = '287380a40abd'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('yarn', 'yarns')


def downgrade():
    pass
