"""rathada

Revision ID: 25b6580be231
Revises: b66c8fd820fa
Create Date: 2020-03-30 05:03:48.936991

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '25b6580be231'
down_revision = 'b66c8fd820fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('address', 'apt',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('address', 'apt',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    # ### end Alembic commands ###