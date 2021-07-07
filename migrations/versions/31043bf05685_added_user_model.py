"""added user model

Revision ID: 31043bf05685
Revises: a45cb4560be9
Create Date: 2020-11-28 13:22:37.737819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31043bf05685'
down_revision = 'a45cb4560be9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=254), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
