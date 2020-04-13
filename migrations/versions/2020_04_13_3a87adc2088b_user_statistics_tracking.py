"""User statistics tracking

Revision ID: 3a87adc2088b
Revises: 7de7ec98049b
Create Date: 2020-04-13 22:11:20.064789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3a87adc2088b"
down_revision = "7de7ec98049b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_statistic",
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("callback_calls", sa.Integer(), nullable=False),
        sa.Column("poll_callback_calls", sa.Integer(), nullable=False),
        sa.Column("created_polls", sa.Integer(), nullable=False),
        sa.Column("inline_shares", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="user", ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("date", "user_id"),
    )
    op.create_index(
        op.f("ix_user_statistic_user_id"), "user_statistic", ["user_id"], unique=False
    )
    op.alter_column(
        "update",
        "count",
        existing_type=sa.INTEGER(),
        server_default=None,
        existing_nullable=False,
    )
    op.add_column(
        "user",
        sa.Column("banned", sa.Boolean(), server_default="FALSE", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "banned")
    op.alter_column(
        "update",
        "count",
        existing_type=sa.INTEGER(),
        server_default=sa.text("0"),
        existing_nullable=False,
    )
    op.drop_index(op.f("ix_user_statistic_user_id"), table_name="user_statistic")
    op.drop_table("user_statistic")
    # ### end Alembic commands ###
