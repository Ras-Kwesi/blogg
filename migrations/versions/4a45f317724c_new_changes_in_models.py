"""new changes in models

Revision ID: 4a45f317724c
Revises: 
Create Date: 2018-09-15 16:42:35.665196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a45f317724c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('post', sa.String(length=255), nullable=True))
    op.add_column('blogs', sa.Column('title', sa.String(length=255), nullable=True))
    op.drop_column('blogs', 'blog')
    op.add_column('users', sa.Column('career', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('nationality', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'nationality')
    op.drop_column('users', 'career')
    op.add_column('blogs', sa.Column('blog', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('blogs', 'title')
    op.drop_column('blogs', 'post')
    # ### end Alembic commands ###
