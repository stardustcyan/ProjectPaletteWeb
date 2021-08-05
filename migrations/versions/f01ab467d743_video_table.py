"""video table

Revision ID: f01ab467d743
Revises: 6db7558b0d67
Create Date: 2021-05-21 10:59:26.775680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f01ab467d743'
down_revision = '6db7558b0d67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('face', sa.String(length=140), nullable=True))
    op.create_index(op.f('ix_video_timestamp'), 'video', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_timestamp'), table_name='video')
    op.drop_column('video', 'face')
    # ### end Alembic commands ###