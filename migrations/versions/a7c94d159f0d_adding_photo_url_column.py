"""Adding photo_url column

Revision ID: a7c94d159f0d
Revises: 01c774450bc0
Create Date: 2023-02-16 01:31:05.554759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7c94d159f0d'
down_revision = '01c774450bc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tour', sa.Column('photo_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tour', 'photo_url')
    # ### end Alembic commands ###
