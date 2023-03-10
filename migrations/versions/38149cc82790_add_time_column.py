"""add time column

Revision ID: 38149cc82790
Revises: a7c94d159f0d
Create Date: 2023-02-17 23:48:16.607897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38149cc82790'
down_revision = 'a7c94d159f0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tour', sa.Column('time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tour', 'time')
    # ### end Alembic commands ###
