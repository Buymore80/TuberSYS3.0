# TuberSYS 3.0 - ERP Ultra Complet

## 🎯 Description

TuberSYS 3.0 est un système ERP (Enterprise Resource Planning) ultra complet développé avec Python Flask. Il intègre un système d'authentification sécurisé et un système de permissions granulaires permettant de contrôler l'accès de chaque utilisateur à des modules spécifiques.

## ✨ Fonctionnalités Principales

### 🔐 Système d'Authentification et Permissions
- **Authentification sécurisée** avec hashage des mots de passe (bcrypt)
- **Gestion des utilisateurs** avec rôles (Admin / Utilisateur standard)
- **Permissions par module** : choisissez précisément quels modules sont accessibles pour chaque utilisateur
- Les administrateurs ont accès à tous les modules automatiquement

### 📊 Modules ERP Intégrés

#### PILOTAGE
- **Dashboard** : Vue d'ensemble avec KPIs en temps réel
- **Statistiques** : Analyses et rapports détaillés
- **Alertes & Anomalies** : Surveillance et gestion des alertes

#### RÉFÉRENTIELS
- **Catalogue Produits** : Gestion des produits et variétés
- **Conditionnements & Formats** : Gestion des formats de conditionnement
- **Fournisseurs** : Base de données fournisseurs
- **Clients** : Gestion de la base clients
- **Transporteurs** : Gestion des transporteurs et véhicules

#### OPÉRATIONS PDT
- **Réceptions** : Gestion des réceptions de marchandises
- **Gestion des Lots** : Traçabilité complète des lots
- **Stocks & Frigos** : Gestion des stocks et chambres froides
- **Suivi Laveuses** : Suivi des machines de lavage

#### COMMERCE
- **Ventes (BC/BL)** : Bons de commande et bons de livraison
- **Grilles Tarifaires** : Gestion des tarifs et prix
- **Facturation** : Gestion complète des factures

#### TECHNIQUE & QUALITÉ
- **GMAO / Tech** : Gestion de la maintenance assistée par ordinateur
- **Qualité & Analyse** : Contrôle qualité et analyses
- **Assistant TuberSys** : Assistant intelligent

### 💾 Base de Données SQLite

**Avantages de SQLite :**
- ✅ **Aucune installation de serveur SQL nécessaire**
- ✅ **Un seul fichier `.db` contenant toutes les données**
- ✅ **Facile à sauvegarder** (copier le fichier)
- ✅ **Parfait pour le partage multi-PC** (voir section ci-dessous)

## 🖥️ Partage Multi-PC

### Solution 1 : Dossier Réseau Partagé (Recommandé pour LAN)

1. Créez un dossier partagé sur votre réseau (ex: `\\\\SERVEUR\\TuberSYS`)
2. Modifiez le fichier `.env` :
   ```env
   DATABASE_PATH=\\\\SERVEUR\\TuberSYS\\data\\tubersys.db
   ```

### Solution 2 : Cloud (Dropbox, OneDrive, Google Drive)

1. Installez Dropbox, OneDrive ou Google Drive
2. Placez le dossier `data` dans le dossier synchronisé
3. Modifiez le fichier `.env` :
   ```env
   # Windows
   DATABASE_PATH=C:\\Users\\YourName\\Dropbox\\TuberSYS\\data\\tubersys.db

   # Linux
   DATABASE_PATH=/home/username/Dropbox/TuberSYS/data/tubersys.db
   ```

### Solution 3 : Serveur Web Central (Pour équipes distantes)

Déployez l'application sur un serveur web central accessible par tous les utilisateurs.

## 📦 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'Installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd TuberSYS3.0
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer l'environnement**
   ```bash
   cp .env.example .env
   ```

   Éditez le fichier `.env` et modifiez les paramètres selon vos besoins :
   ```env
   SECRET_KEY=votre-cle-ultra-secrete-a-changer
   DATABASE_PATH=./data/tubersys.db
   ```

4. **Lancer l'application**
   ```bash
   python app.py
   ```

5. **Accéder à l'application**

   Ouvrez votre navigateur et allez sur : `http://localhost:5000`

## 🔑 Connexion par Défaut

Lors du premier lancement, un compte administrateur est créé automatiquement :

- **Nom d'utilisateur** : `admin`
- **Mot de passe** : `admin123`

⚠️ **IMPORTANT** : Changez ce mot de passe dès la première connexion !

## 👥 Gestion des Utilisateurs

### Créer un Nouvel Utilisateur

1. Connectez-vous en tant qu'administrateur
2. Allez dans **Administration** > **Gestion des Utilisateurs**
3. Cliquez sur **Nouvel Utilisateur**
4. Remplissez le formulaire :
   - Nom d'utilisateur (unique)
   - Nom complet
   - Email
   - Mot de passe
   - Cochez "Administrateur" si nécessaire
5. Cliquez sur **Créer l'utilisateur**

### Définir les Permissions d'un Utilisateur

1. Allez dans **Administration** > **Gestion des Utilisateurs**
2. Cliquez sur **Permissions** à côté de l'utilisateur
3. Sélectionnez les modules auxquels l'utilisateur aura accès
4. Cliquez sur **Enregistrer les Permissions**

**Notes :**
- Les administrateurs ont accès à tous les modules automatiquement
- Les utilisateurs sans permissions ne verront aucun module dans le menu
- Les permissions peuvent être modifiées à tout moment

## 🎨 Interface

L'interface utilise un thème sombre moderne avec :
- Sidebar de navigation avec icônes
- Dashboard avec KPIs
- Tableaux de données interactifs
- Design responsive (fonctionne sur mobile/tablette)

## 🛠️ Technologies Utilisées

- **Backend** : Python 3, Flask
- **Base de données** : SQLite
- **ORM** : Flask-SQLAlchemy
- **Authentification** : Flask-Login
- **Hashage de mot de passe** : bcrypt
- **Frontend** : HTML5, CSS3, JavaScript
- **Icônes** : Font Awesome
- **Polices** : Inter (Google Fonts)

## 📁 Structure du Projet

```
TuberSYS3.0/
├── app.py                  # Application Flask principale
├── database.py             # Configuration de la base de données
├── models.py               # Modèles de données (User, Module, etc.)
├── requirements.txt        # Dépendances Python
├── .env                    # Configuration (à créer)
├── .env.example           # Exemple de configuration
├── data/                   # Dossier de la base de données
│   └── tubersys.db        # Fichier SQLite (créé automatiquement)
├── templates/             # Templates HTML
│   ├── base.html         # Template de base
│   ├── login.html        # Page de connexion
│   ├── dashboard.html    # Dashboard principal
│   ├── admin/            # Templates d'administration
│   │   ├── index.html
│   │   ├── users.html
│   │   ├── create_user.html
│   │   └── user_permissions.html
│   └── modules/          # Templates des modules ERP
│       ├── clients.html
│       ├── catalogue_produits.html
│       ├── fournisseurs.html
│       └── ...
└── static/               # Fichiers statiques
    ├── css/
    │   └── style.css    # Styles CSS
    ├── js/
    │   └── main.js      # JavaScript
    └── img/             # Images
```

## 🔒 Sécurité

- ✅ Mots de passe hashés avec bcrypt
- ✅ Protection contre les injections SQL (SQLAlchemy ORM)
- ✅ Sessions sécurisées (Flask-Login)
- ✅ CSRF protection (Flask-WTF)
- ✅ Gestion fine des permissions

## 📊 Sauvegarde des Données

Pour sauvegarder vos données, copiez simplement le fichier :
```
data/tubersys.db
```

Pour restaurer, replacez le fichier au même endroit.

**Recommandation** : Configurez des sauvegardes automatiques quotidiennes.

## 🚀 Développement Futur

Le système est conçu pour être extensible. Vous pouvez :
- Ajouter de nouveaux modules
- Personnaliser les formulaires
- Ajouter des rapports PDF
- Intégrer des graphiques interactifs
- Connecter des APIs externes

## 💡 Conseils d'Utilisation

1. **Premier démarrage** : Créez les utilisateurs et définissez leurs permissions
2. **Multi-PC** : Configurez le DATABASE_PATH vers un dossier partagé
3. **Sécurité** : Changez la SECRET_KEY dans `.env` en production
4. **Performance** : Pour de très grosses bases, envisagez PostgreSQL

## 📞 Support

Pour toute question ou problème :
- Consultez ce README
- Vérifiez les logs de l'application
- Assurez-vous que tous les utilisateurs ont les bonnes permissions

## 📝 Licence

Ce projet est développé pour TuberSYS. Tous droits réservés.

---

**Version** : 3.0
**Date** : 2026
**Développé avec** : ❤️ et Python
