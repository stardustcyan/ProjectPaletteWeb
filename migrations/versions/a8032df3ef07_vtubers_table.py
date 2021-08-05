"""vtubers table

Revision ID: a8032df3ef07
Revises: 
Create Date: 2021-04-08 14:57:51.712464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8032df3ef07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_name'), 'group', ['name'], unique=False)
    op.create_table('vtuber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vtuber_name'), 'vtuber', ['name'], unique=True)
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=140), nullable=True),
    sa.Column('vtuber_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['vtuber_id'], ['vtuber.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('video')
    op.drop_index(op.f('ix_vtuber_name'), table_name='vtuber')
    op.drop_table('vtuber')
    op.drop_index(op.f('ix_group_name'), table_name='group')
    op.drop_table('group')
    # ### end Alembic commands ###