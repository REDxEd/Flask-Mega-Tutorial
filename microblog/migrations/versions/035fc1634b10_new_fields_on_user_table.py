"""new fields on User table

Revision ID: 035fc1634b10
Revises: 7cfc7b3566ae
Create Date: 2022-10-12 21:19:42.186726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '035fc1634b10'
down_revision = '7cfc7b3566ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###