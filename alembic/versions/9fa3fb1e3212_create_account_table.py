"""create account table

Revision ID: 9fa3fb1e3212
Revises: 
Create Date: 2019-03-18 14:22:46.999713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fa3fb1e3212'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'yarn',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('superwash', sa.Boolean),
        sa.Column('yardage', sa.Integer),
        sa.Column('notes', sa.String(100)),
    )


def downgrade():
    op.drop_table('yarn')
