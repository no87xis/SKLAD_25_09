"""Add new fields to Order: eur_rate, client_city, payment_method, payment_note

Revision ID: 001
Revises: 000
Create Date: 2025-08-28 12:45:19.303055

"""
from alembic import op
import sqlalchemy as sa
from decimal import Decimal


# revision identifiers, used by Alembic.
revision = '001'
down_revision = '000'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Поля уже добавлены в initial миграции 000
    # Эта миграция оставлена для совместимости
    pass


def downgrade() -> None:
    # Поля уже есть в initial миграции
    pass
