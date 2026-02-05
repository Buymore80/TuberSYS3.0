"""
TuberSYS 3.0 - ERP Ultra Complet
Système de gestion intégré avec authentification et permissions par module
"""

from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Construire le chemin absolu de la base de données basé sur l'emplacement du script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'tubersys.db')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation des extensions
from database import db, login_manager

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'

# Import des modèles après l'initialisation de db
from models import User, Module, UserPermission, Client, Product, Supplier, Invoice, Stock, Order

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ======================
# ROUTES D'AUTHENTIFICATION
# ======================

@app.route('/')
def index():
    """Page d'accueil - redirige vers login ou dashboard"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Page de connexion"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            if not user.is_active:
                flash('Votre compte est désactivé. Contactez l\'administrateur.', 'danger')
                return redirect(url_for('login'))

            login_user(user, remember=request.form.get('remember', False))
            flash(f'Bienvenue {user.full_name} !', 'success')

            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('dashboard'))
        else:
            flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Déconnexion"""
    logout_user()
    flash('Vous avez été déconnecté avec succès.', 'info')
    return redirect(url_for('login'))

# ======================
# DASHBOARD PRINCIPAL
# ======================

@app.route('/dashboard')
@login_required
def dashboard():
    """Tableau de bord principal"""
    # Vérifier si l'utilisateur a accès au dashboard
    if not current_user.has_permission('dashboard'):
        flash('Vous n\'avez pas accès au tableau de bord.', 'danger')
        return redirect(url_for('no_permission'))

    # Calculer les KPIs
    stats = {
        'stock_total': Stock.query.with_entities(db.func.sum(Stock.quantity)).scalar() or 0,
        'trs_estime': 0,  # À calculer selon votre logique
        'expeditions_jour': Order.query.filter(
            db.func.date(Order.created_at) == datetime.now().date()
        ).count(),
        'maintenance': 0,  # À implémenter
        'total_clients': Client.query.count(),
        'total_products': Product.query.count(),
        'total_suppliers': Supplier.query.count(),
        'total_invoices': Invoice.query.count(),
    }

    return render_template('dashboard.html', stats=stats)

# ======================
# MODULES - PILOTAGE
# ======================

@app.route('/statistiques')
@login_required
def statistiques():
    """Module Statistiques"""
    if not current_user.has_permission('statistiques'):
        return redirect(url_for('no_permission'))
    return render_template('modules/statistiques.html')

@app.route('/alertes')
@login_required
def alertes():
    """Module Alertes & Anomalies"""
    if not current_user.has_permission('alertes'):
        return redirect(url_for('no_permission'))
    return render_template('modules/alertes.html')

# ======================
# MODULES - RÉFÉRENTIELS
# ======================

@app.route('/catalogue-produits')
@login_required
def catalogue_produits():
    """Module Catalogue Produits"""
    if not current_user.has_permission('catalogue_produits'):
        return redirect(url_for('no_permission'))

    products = Product.query.all()
    return render_template('modules/catalogue_produits.html', products=products)

@app.route('/conditionnements')
@login_required
def conditionnements():
    """Module Conditionnements & Formats"""
    if not current_user.has_permission('conditionnements'):
        return redirect(url_for('no_permission'))
    return render_template('modules/conditionnements.html')

@app.route('/fournisseurs')
@login_required
def fournisseurs():
    """Module Fournisseurs"""
    if not current_user.has_permission('fournisseurs'):
        return redirect(url_for('no_permission'))

    suppliers = Supplier.query.all()
    return render_template('modules/fournisseurs.html', suppliers=suppliers)

@app.route('/clients')
@login_required
def clients():
    """Module Clients"""
    if not current_user.has_permission('clients'):
        return redirect(url_for('no_permission'))

    clients = Client.query.all()
    return render_template('modules/clients.html', clients=clients)

@app.route('/transporteurs')
@login_required
def transporteurs():
    """Module Transporteurs"""
    if not current_user.has_permission('transporteurs'):
        return redirect(url_for('no_permission'))
    return render_template('modules/transporteurs.html')

# ======================
# MODULES - OPÉRATIONS PDT
# ======================

@app.route('/receptions')
@login_required
def receptions():
    """Module Réceptions"""
    if not current_user.has_permission('receptions'):
        return redirect(url_for('no_permission'))
    return render_template('modules/receptions.html')

@app.route('/gestion-lots')
@login_required
def gestion_lots():
    """Module Gestion des Lots"""
    if not current_user.has_permission('gestion_lots'):
        return redirect(url_for('no_permission'))
    return render_template('modules/gestion_lots.html')

@app.route('/stocks-frigos')
@login_required
def stocks_frigos():
    """Module Stocks & Frigos"""
    if not current_user.has_permission('stocks_frigos'):
        return redirect(url_for('no_permission'))

    stocks = Stock.query.all()
    return render_template('modules/stocks_frigos.html', stocks=stocks)

@app.route('/suivi-laveuses')
@login_required
def suivi_laveuses():
    """Module Suivi Laveuses"""
    if not current_user.has_permission('suivi_laveuses'):
        return redirect(url_for('no_permission'))
    return render_template('modules/suivi_laveuses.html')

# ======================
# MODULES - COMMERCE
# ======================

@app.route('/ventes')
@login_required
def ventes():
    """Module Ventes (BC/BL)"""
    if not current_user.has_permission('ventes'):
        return redirect(url_for('no_permission'))

    orders = Order.query.all()
    return render_template('modules/ventes.html', orders=orders)

@app.route('/grilles-tarifaires')
@login_required
def grilles_tarifaires():
    """Module Grilles Tarifaires"""
    if not current_user.has_permission('grilles_tarifaires'):
        return redirect(url_for('no_permission'))
    return render_template('modules/grilles_tarifaires.html')

@app.route('/facturation')
@login_required
def facturation():
    """Module Facturation"""
    if not current_user.has_permission('facturation'):
        return redirect(url_for('no_permission'))

    invoices = Invoice.query.all()
    return render_template('modules/facturation.html', invoices=invoices)

# ======================
# MODULES - TECHNIQUE & QUALITÉ
# ======================

@app.route('/gmao-tech')
@login_required
def gmao_tech():
    """Module GMAO / Tech"""
    if not current_user.has_permission('gmao_tech'):
        return redirect(url_for('no_permission'))
    return render_template('modules/gmao_tech.html')

@app.route('/qualite-analyse')
@login_required
def qualite_analyse():
    """Module Qualité & Analyse"""
    if not current_user.has_permission('qualite_analyse'):
        return redirect(url_for('no_permission'))
    return render_template('modules/qualite_analyse.html')

@app.route('/assistant-tubersys')
@login_required
def assistant_tubersys():
    """Module Assistant TuberSys"""
    if not current_user.has_permission('assistant_tubersys'):
        return redirect(url_for('no_permission'))
    return render_template('modules/assistant_tubersys.html')

# ======================
# ADMINISTRATION
# ======================

@app.route('/admin')
@login_required
def admin():
    """Panel d'administration (réservé aux administrateurs)"""
    if not current_user.is_admin:
        flash('Accès réservé aux administrateurs.', 'danger')
        return redirect(url_for('dashboard'))

    users = User.query.all()
    modules = Module.query.all()
    return render_template('admin/index.html', users=users, modules=modules)

@app.route('/admin/users')
@login_required
def admin_users():
    """Gestion des utilisateurs"""
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))

    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/users/create', methods=['GET', 'POST'])
@login_required
def admin_create_user():
    """Créer un nouvel utilisateur"""
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        password = request.form.get('password')
        is_admin = request.form.get('is_admin') == 'on'

        # Vérifier si l'utilisateur existe déjà
        if User.query.filter_by(username=username).first():
            flash('Ce nom d\'utilisateur existe déjà.', 'danger')
            return redirect(url_for('admin_create_user'))

        if User.query.filter_by(email=email).first():
            flash('Cet email existe déjà.', 'danger')
            return redirect(url_for('admin_create_user'))

        # Créer l'utilisateur
        user = User(
            username=username,
            email=email,
            full_name=full_name,
            password_hash=generate_password_hash(password),
            is_admin=is_admin
        )

        db.session.add(user)
        db.session.commit()

        flash(f'Utilisateur {username} créé avec succès !', 'success')
        return redirect(url_for('admin_users'))

    return render_template('admin/create_user.html')

@app.route('/admin/users/<int:user_id>/permissions', methods=['GET', 'POST'])
@login_required
def admin_user_permissions(user_id):
    """Gérer les permissions d'un utilisateur"""
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))

    user = User.query.get_or_404(user_id)
    modules = Module.query.all()

    if request.method == 'POST':
        # Supprimer toutes les permissions existantes
        UserPermission.query.filter_by(user_id=user_id).delete()

        # Ajouter les nouvelles permissions
        for module in modules:
            if request.form.get(f'module_{module.id}'):
                permission = UserPermission(user_id=user_id, module_id=module.id)
                db.session.add(permission)

        db.session.commit()
        flash(f'Permissions mises à jour pour {user.username}', 'success')
        return redirect(url_for('admin_users'))

    # Récupérer les permissions actuelles
    user_permissions = {p.module_id for p in user.permissions}

    return render_template('admin/user_permissions.html',
                         user=user,
                         modules=modules,
                         user_permissions=user_permissions)

@app.route('/admin/users/<int:user_id>/toggle-active', methods=['POST'])
@login_required
def admin_toggle_user_active(user_id):
    """Activer/désactiver un utilisateur"""
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403

    user = User.query.get_or_404(user_id)
    user.is_active = not user.is_active
    db.session.commit()

    status = 'activé' if user.is_active else 'désactivé'
    return jsonify({'success': True, 'message': f'Utilisateur {status}', 'is_active': user.is_active})

@app.route('/no-permission')
@login_required
def no_permission():
    """Page affichée quand l'utilisateur n'a pas les permissions"""
    return render_template('no_permission.html')

# ======================
# API ENDPOINTS (pour AJAX)
# ======================

@app.route('/api/products', methods=['GET', 'POST'])
@login_required
def api_products():
    """API pour gérer les produits"""
    if request.method == 'GET':
        products = Product.query.all()
        return jsonify([p.to_dict() for p in products])

    elif request.method == 'POST':
        data = request.get_json()
        product = Product(
            name=data.get('name'),
            reference=data.get('reference'),
            category=data.get('category'),
            price=data.get('price', 0)
        )
        db.session.add(product)
        db.session.commit()
        return jsonify(product.to_dict()), 201

@app.route('/api/clients', methods=['GET', 'POST'])
@login_required
def api_clients():
    """API pour gérer les clients"""
    if request.method == 'GET':
        clients = Client.query.all()
        return jsonify([c.to_dict() for c in clients])

    elif request.method == 'POST':
        data = request.get_json()
        client = Client(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address')
        )
        db.session.add(client)
        db.session.commit()
        return jsonify(client.to_dict()), 201

# ======================
# FILTRES JINJA
# ======================

@app.template_filter('format_date')
def format_date(date):
    """Formater une date"""
    if date:
        return date.strftime('%d/%m/%Y')
    return ''

@app.template_filter('format_datetime')
def format_datetime(date):
    """Formater une date avec heure"""
    if date:
        return date.strftime('%d/%m/%Y %H:%M')
    return ''

@app.template_filter('format_currency')
def format_currency(amount):
    """Formater un montant en euros"""
    return f"{amount:,.2f} €".replace(',', ' ')

# ======================
# INITIALISATION
# ======================

def init_db():
    """Initialiser la base de données"""
    with app.app_context():
        # Créer le dossier data s'il n'existe pas (utilise le même chemin que la config)
        db_dir = os.path.join(BASE_DIR, 'data')
        os.makedirs(db_dir, exist_ok=True)

        print(f"📁 Dossier de la base de données : {db_dir}")
        print(f"📄 Fichier de la base de données : {DB_PATH}")

        # Créer les tables
        db.create_all()

        # Créer les modules si ils n'existent pas
        if Module.query.count() == 0:
            modules = [
                # PILOTAGE
                Module(code='dashboard', name='Dashboard', category='PILOTAGE', icon='fa-th-large', order=1),
                Module(code='statistiques', name='Statistiques', category='PILOTAGE', icon='fa-chart-bar', order=2),
                Module(code='alertes', name='Alertes & Anomalies', category='PILOTAGE', icon='fa-exclamation-triangle', order=3),

                # RÉFÉRENTIELS
                Module(code='catalogue_produits', name='Catalogue Produits', category='RÉFÉRENTIELS', icon='fa-tag', order=4),
                Module(code='conditionnements', name='Cond. Formats', category='RÉFÉRENTIELS', icon='fa-box', order=5),
                Module(code='fournisseurs', name='Fournisseurs', category='RÉFÉRENTIELS', icon='fa-truck', order=6),
                Module(code='clients', name='Clients', category='RÉFÉRENTIELS', icon='fa-users', order=7),
                Module(code='transporteurs', name='Transporteurs', category='RÉFÉRENTIELS', icon='fa-shipping-fast', order=8),

                # OPÉRATIONS PDT
                Module(code='receptions', name='Réceptions', category='OPÉRATIONS PDT', icon='fa-inbox', order=9),
                Module(code='gestion_lots', name='Gestion des Lots', category='OPÉRATIONS PDT', icon='fa-clipboard-list', order=10),
                Module(code='stocks_frigos', name='Stocks & Frigos', category='OPÉRATIONS PDT', icon='fa-warehouse', order=11),
                Module(code='suivi_laveuses', name='Suivi Laveuses', category='OPÉRATIONS PDT', icon='fa-tint', order=12),

                # COMMERCE
                Module(code='ventes', name='Ventes (BC/BL)', category='COMMERCE', icon='fa-shopping-cart', order=13),
                Module(code='grilles_tarifaires', name='Grilles Tarifaires', category='COMMERCE', icon='fa-file-invoice-dollar', order=14),
                Module(code='facturation', name='Facturation', category='COMMERCE', icon='fa-file-invoice', order=15),

                # TECHNIQUE & QUALITÉ
                Module(code='gmao_tech', name='GMAO / Tech', category='TECHNIQUE & QUALITÉ', icon='fa-wrench', order=16),
                Module(code='qualite_analyse', name='Qualité & Analyse', category='TECHNIQUE & QUALITÉ', icon='fa-microscope', order=17),
                Module(code='assistant_tubersys', name='Assistant TuberSys', category='TECHNIQUE & QUALITÉ', icon='fa-robot', order=18),
            ]

            for module in modules:
                db.session.add(module)

            db.session.commit()
            print("✅ Modules créés avec succès")

        # Créer un utilisateur admin par défaut
        if User.query.filter_by(username='admin').first() is None:
            admin = User(
                username='admin',
                email='admin@tubersys.com',
                full_name='Administrateur',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()

            # Donner tous les droits à l'admin
            modules = Module.query.all()
            for module in modules:
                permission = UserPermission(user_id=admin.id, module_id=module.id)
                db.session.add(permission)

            db.session.commit()
            print("✅ Utilisateur admin créé (login: admin / password: admin123)")

if __name__ == '__main__':
    init_db()
    print("\n" + "="*50)
    print("🚀 TuberSYS 3.0 - ERP Ultra Complet")
    print("="*50)
    print("\n📝 Connexion par défaut:")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n🌐 Accédez à l'application sur: http://localhost:5000")
    print("="*50 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
