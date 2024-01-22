"""projects table

Revision ID: 6374d731b59f
Revises: fca8211435fd
Create Date: 2024-01-22 20:43:35.924907

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6374d731b59f"
down_revision = "fca8211435fd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.String(length=140), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["account.id"], name=op.f("fk_project_user_id_account")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_project")),
    )
    with op.batch_alter_table("project", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_project_timestamp"), ["timestamp"], unique=False
        )
        batch_op.create_index(
            batch_op.f("ix_project_user_id"), ["user_id"], unique=False
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("project", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_project_user_id"))
        batch_op.drop_index(batch_op.f("ix_project_timestamp"))

    op.drop_table("project")
    # ### end Alembic commands ###