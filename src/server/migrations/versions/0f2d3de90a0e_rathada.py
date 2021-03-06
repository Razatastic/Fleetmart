"""rathada

Revision ID: 0f2d3de90a0e
Revises: e31ad3e33bbf
Create Date: 2020-03-30 05:23:31.397172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f2d3de90a0e'
down_revision = 'e31ad3e33bbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('zip_code', table_name='address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('zip_code', 'address', ['zip_code'], unique=True)
    # ### end Alembic commands ###
