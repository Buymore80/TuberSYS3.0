"""
Configuration de la base de données
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialisation des extensions
db = SQLAlchemy()
login_manager = LoginManager()
