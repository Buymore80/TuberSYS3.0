"""
Modèles de base de données pour TuberSYS 3.0
Utilise SQLite pour faciliter le partage entre plusieurs PC
"""

from flask_login import UserMixin
from datetime import datetime
from database import db

# ======================
# UTILISATEURS ET PERMISSIONS
# ======================

class User(UserMixin, db.Model):
    """Modèle Utilisateur avec système d'authentification"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    # Relations
    permissions = db.relationship('UserPermission', backref='user', lazy=True, cascade='all, delete-orphan')

    def has_permission(self, module_code):
        """Vérifier si l'utilisateur a accès à un module"""
        if self.is_admin:
            return True

        module = Module.query.filter_by(code=module_code).first()
        if not module:
            return False

        return UserPermission.query.filter_by(
            user_id=self.id,
            module_id=module.id
        ).first() is not None

    def get_accessible_modules(self):
        """Récupérer tous les modules accessibles par l'utilisateur"""
        if self.is_admin:
            return Module.query.order_by(Module.order).all()

        module_ids = [p.module_id for p in self.permissions]
        return Module.query.filter(Module.id.in_(module_ids)).order_by(Module.order).all()

    def __repr__(self):
        return f'<User {self.username}>'


class Module(db.Model):
    """Modèle Module - Représente les différents modules de l'ERP"""
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # PILOTAGE, RÉFÉRENTIELS, etc.
    icon = db.Column(db.String(50), default='fa-circle')
    order = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    # Relations
    permissions = db.relationship('UserPermission', backref='module', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Module {self.code}>'


class UserPermission(db.Model):
    """Modèle Permission - Association entre User et Module"""
    __tablename__ = 'user_permissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'), nullable=False)
    granted_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Index unique pour éviter les doublons
    __table_args__ = (db.UniqueConstraint('user_id', 'module_id', name='unique_user_module'),)

    def __repr__(self):
        return f'<Permission User:{self.user_id} Module:{self.module_id}>'


# ======================
# CLIENTS
# ======================

class Client(db.Model):
    """Modèle Client"""
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(50), default='France')
    siret = db.Column(db.String(14))
    tva_number = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    orders = db.relationship('Order', backref='client', lazy=True)
    invoices = db.relationship('Invoice', backref='client', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'postal_code': self.postal_code,
            'is_active': self.is_active
        }

    def __repr__(self):
        return f'<Client {self.name}>'


# ======================
# PRODUITS
# ======================

class Product(db.Model):
    """Modèle Produit"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    variety = db.Column(db.String(100))  # Variété (pomme de terre, etc.)
    unit = db.Column(db.String(20), default='kg')  # kg, tonne, unité
    price = db.Column(db.Float, default=0.0)
    cost_price = db.Column(db.Float, default=0.0)
    barcode = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    stocks = db.relationship('Stock', backref='product', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'reference': self.reference,
            'name': self.name,
            'category': self.category,
            'variety': self.variety,
            'unit': self.unit,
            'price': self.price,
            'is_active': self.is_active
        }

    def __repr__(self):
        return f'<Product {self.reference} - {self.name}>'


# ======================
# FOURNISSEURS
# ======================

class Supplier(db.Model):
    """Modèle Fournisseur"""
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(50), default='France')
    siret = db.Column(db.String(14))
    tva_number = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'phone': self.phone,
            'is_active': self.is_active
        }

    def __repr__(self):
        return f'<Supplier {self.name}>'


# ======================
# STOCKS
# ======================

class Stock(db.Model):
    """Modèle Stock"""
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    location = db.Column(db.String(100))  # Frigo 1, Zone A, etc.
    lot_number = db.Column(db.String(50))
    quantity = db.Column(db.Float, default=0.0)
    unit = db.Column(db.String(20), default='kg')
    min_quantity = db.Column(db.Float, default=0.0)  # Seuil d'alerte
    expiry_date = db.Column(db.Date)
    reception_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def is_low_stock(self):
        """Vérifier si le stock est bas"""
        return self.quantity <= self.min_quantity

    def __repr__(self):
        return f'<Stock Product:{self.product_id} Qty:{self.quantity}>'


# ======================
# COMMANDES / VENTES
# ======================

class Order(db.Model):
    """Modèle Commande / Vente"""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(50), unique=True, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, confirmed, shipped, delivered, cancelled
    order_type = db.Column(db.String(20), default='BC')  # BC (Bon de Commande) ou BL (Bon de Livraison)
    total_amount = db.Column(db.Float, default=0.0)
    tax_amount = db.Column(db.Float, default=0.0)
    notes = db.Column(db.Text)
    delivery_date = db.Column(db.Date)
    delivery_address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Order {self.order_number}>'


class OrderItem(db.Model):
    """Modèle Ligne de commande"""
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text)

    # Relation
    product = db.relationship('Product', backref='order_items')

    def __repr__(self):
        return f'<OrderItem Order:{self.order_id} Product:{self.product_id}>'


# ======================
# FACTURES
# ======================

class Invoice(db.Model):
    """Modèle Facture"""
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(50), unique=True, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    issue_date = db.Column(db.Date, default=datetime.utcnow)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(50), default='pending')  # pending, paid, overdue, cancelled
    subtotal = db.Column(db.Float, default=0.0)
    tax_rate = db.Column(db.Float, default=20.0)  # TVA en %
    tax_amount = db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float, default=0.0)
    paid_amount = db.Column(db.Float, default=0.0)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relation
    order = db.relationship('Order', backref='invoices')

    def __repr__(self):
        return f'<Invoice {self.invoice_number}>'


# ======================
# TRANSPORTEURS
# ======================

class Transporter(db.Model):
    """Modèle Transporteur"""
    __tablename__ = 'transporters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    vehicle_type = db.Column(db.String(100))
    license_plate = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transporter {self.name}>'


# ======================
# LOTS
# ======================

class Lot(db.Model):
    """Modèle Lot de production"""
    __tablename__ = 'lots'

    id = db.Column(db.Integer, primary_key=True)
    lot_number = db.Column(db.String(50), unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    quantity = db.Column(db.Float, nullable=False)
    reception_date = db.Column(db.DateTime, default=datetime.utcnow)
    production_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    quality_status = db.Column(db.String(50), default='pending')  # pending, approved, rejected
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    product = db.relationship('Product', backref='lots')
    supplier = db.relationship('Supplier', backref='lots')

    def __repr__(self):
        return f'<Lot {self.lot_number}>'


# ======================
# ALERTES
# ======================

class Alert(db.Model):
    """Modèle Alerte / Anomalie"""
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    level = db.Column(db.String(20), default='info')  # info, warning, critical
    category = db.Column(db.String(50))  # stock, quality, maintenance, etc.
    is_read = db.Column(db.Boolean, default=False)
    is_resolved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Alert {self.title}>'
