# 🚀 Guide de Démarrage Rapide - TuberSYS 3.0

## Installation en 3 étapes

### 1️⃣ Installer Python et les dépendances

```bash
# Vérifier que Python 3 est installé
python --version

# Installer les dépendances
pip install -r requirements.txt
```

### 2️⃣ Configurer l'application

```bash
# Copier le fichier de configuration
cp .env.example .env

# (Optionnel) Modifier .env pour changer le chemin de la base de données
# Pour partage multi-PC, utilisez un dossier partagé réseau ou cloud
```

### 3️⃣ Lancer l'application

**Option A - Avec le script de démarrage (Recommandé):**
```bash
./start.sh
```

**Option B - Manuellement:**
```bash
python app.py
```

L'application sera accessible sur: **http://localhost:5000**

---

## 🔑 Première Connexion

**Identifiants par défaut:**
- **Nom d'utilisateur:** `admin`
- **Mot de passe:** `admin123`

⚠️ **IMPORTANT:** Changez ce mot de passe dès la première connexion !

---

## 👥 Créer un Nouvel Utilisateur

1. Connectez-vous en tant qu'admin
2. Cliquez sur **Administration** dans le menu
3. Cliquez sur **Créer un Utilisateur**
4. Remplissez le formulaire:
   - Nom d'utilisateur (unique)
   - Nom complet
   - Email
   - Mot de passe
   - Cochez "Administrateur" si nécessaire
5. Cliquez sur **Créer l'utilisateur**

---

## 🔐 Gérer les Permissions d'un Utilisateur

1. Allez dans **Administration** > **Gestion des Utilisateurs**
2. Cliquez sur **Permissions** à côté de l'utilisateur
3. Cochez les modules auxquels l'utilisateur aura accès
4. Cliquez sur **Enregistrer les Permissions**

**Astuce:** Les administrateurs ont automatiquement accès à tous les modules.

---

## 🖥️ Partager entre Plusieurs PC

### Solution 1: Dossier Réseau (LAN)

1. Créez un dossier partagé sur votre réseau (ex: `\\SERVEUR\TuberSYS`)
2. Modifiez `.env` sur **TOUS les PC**:
```env
DATABASE_PATH=\\SERVEUR\TuberSYS\data\tubersys.db
```

### Solution 2: Cloud (Dropbox/OneDrive/Google Drive)

1. Installez Dropbox, OneDrive ou Google Drive
2. Placez le dossier `TuberSYS3.0` dans le dossier synchronisé
3. Sur chaque PC, modifiez `.env`:
```env
# Windows
DATABASE_PATH=C:\Users\VotreNom\Dropbox\TuberSYS3.0\data\tubersys.db

# Linux/Mac
DATABASE_PATH=/home/votrenom/Dropbox/TuberSYS3.0/data/tubersys.db
```

⚠️ **Attention:** Ne lancez pas l'application sur plusieurs PC **en même temps** avec SQLite (risque de corruption). Pour un usage simultané, utilisez PostgreSQL ou MySQL.

---

## 📊 Les Modules Disponibles

### PILOTAGE
- **Dashboard**: Vue d'ensemble avec KPIs
- **Statistiques**: Analyses détaillées
- **Alertes & Anomalies**: Surveillance

### RÉFÉRENTIELS
- **Catalogue Produits**: Gestion des produits
- **Conditionnements**: Formats de conditionnement
- **Fournisseurs**: Base fournisseurs
- **Clients**: Base clients
- **Transporteurs**: Gestion des transporteurs

### OPÉRATIONS PDT
- **Réceptions**: Réceptions de marchandises
- **Gestion des Lots**: Traçabilité
- **Stocks & Frigos**: Gestion des stocks
- **Suivi Laveuses**: Suivi des machines

### COMMERCE
- **Ventes (BC/BL)**: Bons de commande/livraison
- **Grilles Tarifaires**: Gestion des tarifs
- **Facturation**: Facturation complète

### TECHNIQUE & QUALITÉ
- **GMAO / Tech**: Maintenance
- **Qualité & Analyse**: Contrôle qualité
- **Assistant TuberSys**: Assistant intelligent

---

## 💾 Sauvegarder les Données

Pour sauvegarder vos données, copiez simplement:
```
data/tubersys.db
```

Pour restaurer, replacez le fichier au même endroit.

**Recommandation:** Sauvegardez régulièrement (quotidiennement si possible).

---

## ❓ Résolution de Problèmes

### L'application ne démarre pas
- Vérifiez que Python 3.8+ est installé: `python --version`
- Vérifiez que les dépendances sont installées: `pip install -r requirements.txt`

### Je ne peux pas me connecter
- Utilisez les identifiants par défaut: `admin` / `admin123`
- Vérifiez que la base de données existe: `ls data/tubersys.db`

### Un utilisateur ne voit pas certains modules
- Vérifiez ses permissions dans Administration > Gestion des Utilisateurs
- Les administrateurs ont accès à tout automatiquement

### Erreur "unable to open database file"
- Vérifiez le chemin dans `.env`
- Assurez-vous que le dossier existe
- Vérifiez les permissions d'accès

---

## 🔒 Sécurité

- ✅ Les mots de passe sont hashés (bcrypt)
- ✅ Changez la `SECRET_KEY` dans `.env` en production
- ✅ Changez le mot de passe admin par défaut
- ✅ Créez des utilisateurs avec permissions limitées
- ✅ Sauvegardez régulièrement

---

## 📞 Support

Pour toute question:
1. Consultez le `README.md` complet
2. Vérifiez ce guide de démarrage
3. Assurez-vous d'avoir suivi toutes les étapes

---

**Bon travail avec TuberSYS 3.0 !** 🎉
