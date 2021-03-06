"""revision migration to update category and related tables.

Revision ID: 0419907f8237
Revises: 4a84f8b5654f
Create Date: 2020-03-30 01:35:16.934600

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0419907f8237'
down_revision = '4a84f8b5654f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('description', sa.String(length=75), nullable=True))
    op.create_unique_constraint(None, 'category', ['description'])
    op.drop_constraint('category_ibfk_1', 'category', type_='foreignkey')
    op.drop_column('category', 'product_id')
    op.add_column('product', sa.Column('category_id', sa.BigInteger(), nullable=False))
    op.add_column('product', sa.Column('price', sa.Float(), nullable=False))
    op.create_foreign_key(None, 'product', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'price')
    op.drop_column('product', 'category_id')
    op.add_column('category', sa.Column('product_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False))
    op.create_foreign_key('category_ibfk_1', 'category', 'product', ['product_id'], ['id'])
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_column('category', 'description')
    # ### end Alembic commands ###
