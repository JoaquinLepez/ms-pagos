"""initial pagos migration

Revision ID: d9611c2b9f52
Revises: 
Create Date: 2024-11-30 17:37:52.693035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9611c2b9f52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pagos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('medio_pago', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='pagos'
    )
    op.drop_table('alembic_version')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alembic_version',
    sa.Column('version_num', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('version_num', name='alembic_version_pkc')
    )
    op.drop_table('pagos', schema='pagos')
    # ### end Alembic commands ###
