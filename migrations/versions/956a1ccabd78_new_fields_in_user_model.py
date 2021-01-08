"""new fields in user model

Revision ID: 956a1ccabd78
Revises: a00855343f96
Create Date: 2021-01-08 01:28:54.448557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '956a1ccabd78'
down_revision = 'a00855343f96'
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
