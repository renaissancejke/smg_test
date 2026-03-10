"""create links table

Revision ID: 0001_create_links
Revises:
Create Date: 2024-01-01 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0001_create_links"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "links",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("short_id", sa.String(length=10), nullable=False),
        sa.Column("original_url", sa.String(length=2048), nullable=False),
        sa.Column("clicks", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_links_id"), "links", ["id"], unique=False)
    op.create_index(op.f("ix_links_short_id"), "links", ["short_id"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_links_short_id"), table_name="links")
    op.drop_index(op.f("ix_links_id"), table_name="links")
    op.drop_table("links")
