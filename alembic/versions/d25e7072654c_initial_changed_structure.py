"""initial changed structure

Revision ID: d25e7072654c
Revises: 
Create Date: 2019-03-20 19:24:32.920067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd25e7072654c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manufacturers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('materials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('needlesizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('washs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('weights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('yarnshops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('purchased_at', sa.Boolean(), nullable=True),
    sa.Column('notes', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('projectideas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('yardage_needed', sa.Integer(), nullable=True),
    sa.Column('skeins_needed', sa.Integer(), nullable=True),
    sa.Column('weight_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['weight_id'], ['weights.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('swatches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('n_rows', sa.Integer(), nullable=True),
    sa.Column('n_stitches', sa.Integer(), nullable=True),
    sa.Column('n_rows_washed', sa.Integer(), nullable=True),
    sa.Column('n_stiches_washed', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=100), nullable=True),
    sa.Column('needlesize_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['needlesize_id'], ['needlesizes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('yarns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('superwash', sa.Boolean(), nullable=True),
    sa.Column('yardage', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('skeinweight', sa.Integer(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.Column('wash_id', sa.Integer(), nullable=True),
    sa.Column('weight_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturers.id'], ),
    sa.ForeignKeyConstraint(['wash_id'], ['washs.id'], ),
    sa.ForeignKeyConstraint(['weight_id'], ['weights.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('association',
    sa.Column('yarn_id', sa.Integer(), nullable=True),
    sa.Column('material_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['material_id'], ['materials.id'], ),
    sa.ForeignKeyConstraint(['yarn_id'], ['yarns.id'], )
    )
    op.create_table('colorways',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('nr', sa.Integer(), nullable=True),
    sa.Column('in_stash', sa.Boolean(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=100), nullable=True),
    sa.Column('yarn_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['yarn_id'], ['yarns.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('nr')
    )
    op.create_table('work_in_progress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('stichnr', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=200), nullable=True),
    sa.Column('projectidea_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['projectidea_id'], ['projectideas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('yarn_shop_association',
    sa.Column('yarn_id', sa.Integer(), nullable=True),
    sa.Column('yarnshop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['yarn_id'], ['yarns.id'], ),
    sa.ForeignKeyConstraint(['yarnshop_id'], ['yarnshops.id'], )
    )
    op.create_table('yarn_swatch_association',
    sa.Column('yarn_id', sa.Integer(), nullable=True),
    sa.Column('swatch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['swatch_id'], ['swatches.id'], ),
    sa.ForeignKeyConstraint(['yarn_id'], ['yarns.id'], )
    )
    op.create_table('yarns_projectideas_association',
    sa.Column('yarn.id', sa.Integer(), nullable=True),
    sa.Column('projectideas.id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['projectideas.id'], ['projectideas.id'], ),
    sa.ForeignKeyConstraint(['yarn.id'], ['yarns.id'], )
    )
    op.create_table('colorway_work_association',
    sa.Column('colorway_id', sa.Integer(), nullable=True),
    sa.Column('work_in_progress_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['colorway_id'], ['colorways.id'], ),
    sa.ForeignKeyConstraint(['work_in_progress_id'], ['work_in_progress.id'], )
    )
    op.create_table('colorways_projectideas_association',
    sa.Column('colorway_id', sa.Integer(), nullable=True),
    sa.Column('projectidea_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['colorway_id'], ['colorways.id'], ),
    sa.ForeignKeyConstraint(['projectidea_id'], ['projectideas.id'], )
    )
    op.create_table('finished_object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('recipient', sa.String(length=50), nullable=True),
    sa.Column('work_in_progress_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['work_in_progress_id'], ['work_in_progress.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('work_needlesize_association',
    sa.Column('work_in_progress_id', sa.Integer(), nullable=True),
    sa.Column('needlesize_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['needlesize_id'], ['needlesizes.id'], ),
    sa.ForeignKeyConstraint(['work_in_progress_id'], ['work_in_progress.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work_needlesize_association')
    op.drop_table('finished_object')
    op.drop_table('colorways_projectideas_association')
    op.drop_table('colorway_work_association')
    op.drop_table('yarns_projectideas_association')
    op.drop_table('yarn_swatch_association')
    op.drop_table('yarn_shop_association')
    op.drop_table('work_in_progress')
    op.drop_table('colorways')
    op.drop_table('association')
    op.drop_table('yarns')
    op.drop_table('swatches')
    op.drop_table('projectideas')
    op.drop_table('yarnshops')
    op.drop_table('weights')
    op.drop_table('washs')
    op.drop_table('needlesizes')
    op.drop_table('materials')
    op.drop_table('manufacturers')
    # ### end Alembic commands ###