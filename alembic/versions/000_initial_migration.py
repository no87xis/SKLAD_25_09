"""Initial migration - create all tables

Revision ID: 000
Revises: 
Create Date: 2025-01-27 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '000'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create users table
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=True),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('role', sa.Enum('ADMIN', 'MANAGER', 'USER', name='userrole'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )
    
    # Create products table
    op.create_table('products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('detailed_description', sa.Text(), nullable=True),
        sa.Column('price', sa.Numeric(10, 2), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False, default=0),
        sa.Column('min_quantity', sa.Integer(), nullable=False, default=0),
        sa.Column('category', sa.String(100), nullable=True),
        sa.Column('supplier', sa.String(200), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create product_photos table
    op.create_table('product_photos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('photo_path', sa.String(500), nullable=False),
        sa.Column('is_primary', sa.Boolean(), nullable=False, default=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create orders table
    op.create_table('orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order_code', sa.String(50), nullable=True),
        sa.Column('client_name', sa.String(200), nullable=False),
        sa.Column('client_phone', sa.String(20), nullable=True),
        sa.Column('client_city', sa.String(100), nullable=True),
        sa.Column('client_address', sa.Text(), nullable=True),
        sa.Column('total_amount', sa.Numeric(10, 2), nullable=False),
        sa.Column('eur_rate', sa.Numeric(10, 4), nullable=False, server_default='0'),
        sa.Column('payment_method', sa.Enum('UNPAID', 'CASH', 'CARD', 'BANK_TRANSFER', 'QR_CODE', name='paymentmethod'), nullable=False, server_default='UNPAID'),
        sa.Column('payment_note', sa.String(120), nullable=True),
        sa.Column('status', sa.Enum('PENDING', 'CONFIRMED', 'SHIPPED', 'DELIVERED', 'CANCELLED', 'ORDERED_NOT_PAID', name='orderstatus'), nullable=False, default='PENDING'),
        sa.Column('source', sa.String(50), nullable=True),
        sa.Column('qr_code', sa.String(100), nullable=True),
        sa.Column('qr_photo_path', sa.String(500), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create supplies table
    op.create_table('supplies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('supplier_name', sa.String(200), nullable=False),
        sa.Column('supply_date', sa.Date(), nullable=False),
        sa.Column('total_amount', sa.Numeric(10, 2), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create operation_logs table
    op.create_table('operation_logs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('operation_type', sa.String(50), nullable=False),
        sa.Column('entity_type', sa.String(50), nullable=False),
        sa.Column('entity_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('details', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create payment_methods table
    op.create_table('payment_methods',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    
    # Create payment_instruments table
    op.create_table('payment_instruments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('payment_method_id', sa.Integer(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['payment_method_id'], ['payment_methods.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create cash_flows table
    op.create_table('cash_flows',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order_id', sa.Integer(), nullable=True),
        sa.Column('payment_instrument_id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Numeric(10, 2), nullable=False),
        sa.Column('flow_type', sa.Enum('INCOME', 'EXPENSE', name='flowtype'), nullable=False),
        sa.Column('description', sa.String(200), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['payment_instrument_id'], ['payment_instruments.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create shop_carts table
    op.create_table('shop_carts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('session_id', sa.String(100), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create shop_orders table
    op.create_table('shop_orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order_code', sa.String(50), nullable=True),
        sa.Column('client_name', sa.String(200), nullable=False),
        sa.Column('client_phone', sa.String(20), nullable=True),
        sa.Column('client_email', sa.String(100), nullable=True),
        sa.Column('client_address', sa.Text(), nullable=True),
        sa.Column('total_amount', sa.Numeric(10, 2), nullable=False),
        sa.Column('status', sa.Enum('PENDING', 'CONFIRMED', 'SHIPPED', 'DELIVERED', 'CANCELLED', name='shoporderstatus'), nullable=False, default='PENDING'),
        sa.Column('payment_method', sa.String(50), nullable=True),
        sa.Column('delivery_method', sa.String(50), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create product_batches table
    op.create_table('product_batches',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('supply_id', sa.Integer(), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('purchase_price', sa.Numeric(10, 2), nullable=False),
        sa.Column('expiry_date', sa.Date(), nullable=True),
        sa.Column('batch_number', sa.String(100), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['supply_id'], ['supplies.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('product_batches')
    op.drop_table('shop_orders')
    op.drop_table('shop_carts')
    op.drop_table('cash_flows')
    op.drop_table('payment_instruments')
    op.drop_table('payment_methods')
    op.drop_table('operation_logs')
    op.drop_table('supplies')
    op.drop_table('orders')
    op.drop_table('product_photos')
    op.drop_table('products')
    op.drop_table('users')

