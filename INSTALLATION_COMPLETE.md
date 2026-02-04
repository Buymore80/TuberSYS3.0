# 📥 Installation Complète - TuberSYS 3.0
## Depuis GitHub jusqu'au Lancement

---

## 🎯 ÉTAPE 1 : Télécharger le Projet depuis GitHub

### Option A : Téléchargement ZIP (Le Plus Simple) ⭐

1. **Ouvrez votre navigateur web**

2. **Allez sur votre dépôt GitHub :**
   ```
   https://github.com/Buymore80/TuberSYS3.0
   ```

3. **Cliquez sur le bouton vert "Code"** (en haut à droite)

4. **Cliquez sur "Download ZIP"**

5. **Enregistrez le fichier** sur votre ordinateur
   - Windows : `C:\Téléchargements\TuberSYS3.0-main.zip`
   - Mac : `~/Downloads/TuberSYS3.0-main.zip`

6. **Décompressez le fichier ZIP :**
   - **Windows :** Clic droit > "Extraire tout" > Choisissez `C:\TuberSYS3.0`
   - **Mac :** Double-clic sur le fichier ZIP
   - **Linux :** `unzip TuberSYS3.0-main.zip && mv TuberSYS3.0-main TuberSYS3.0`

7. **Vous avez maintenant le dossier :** `TuberSYS3.0` sur votre ordinateur !

---

### Option B : Avec Git Clone (Si Git est Installé)

**Windows (PowerShell) :**
```powershell
cd C:\
git clone https://github.com/Buymore80/TuberSYS3.0.git
```

**Mac/Linux (Terminal) :**
```bash
cd ~
git clone https://github.com/Buymore80/TuberSYS3.0.git
```

---

## 🐍 ÉTAPE 2 : Installer Python (Si Pas Déjà Installé)

### Vérifier si Python est Installé

Ouvrez un terminal/PowerShell et tapez :

```bash
python --version
```

**Si vous voyez** `Python 3.8` ou plus récent → **Python est installé ✅**

**Si vous voyez** une erreur → **Installez Python** :

#### Windows
1. Allez sur https://www.python.org/downloads/
2. Téléchargez Python 3.11 ou plus récent
3. **IMPORTANT :** Cochez "Add Python to PATH" pendant l'installation
4. Suivez l'assistant d'installation

#### Mac
```bash
# Avec Homebrew (recommandé)
brew install python3

# OU téléchargez depuis python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 📦 ÉTAPE 3 : Installer les Dépendances

### Windows (PowerShell)

```powershell
# Aller dans le dossier du projet
cd C:\TuberSYS3.0

# Installer les dépendances
pip install -r requirements.txt
```

### Mac/Linux (Terminal)

```bash
# Aller dans le dossier du projet
cd ~/TuberSYS3.0

# Installer les dépendances
pip3 install -r requirements.txt
```

**Attendez que l'installation se termine** (1-2 minutes)

---

## 🚀 ÉTAPE 4 : Lancer l'Application

### 🌍 Option 1 : Mise en Ligne Automatique (Recommandé)

**Windows :**
```powershell
cd C:\TuberSYS3.0
python lancer_en_ligne.py
```

**Mac/Linux :**
```bash
cd ~/TuberSYS3.0
python3 lancer_en_ligne.py
```

**Vous obtenez une URL publique comme :** `https://abc123.ngrok.io`

---

### 💻 Option 2 : Local Seulement (Sur Votre PC)

**Windows :**
```powershell
cd C:\TuberSYS3.0
python app.py
```

**Mac/Linux :**
```bash
cd ~/TuberSYS3.0
python3 app.py
```

**Ouvrez votre navigateur sur :** `http://localhost:5000`

---

## 🔑 ÉTAPE 5 : Se Connecter

**Identifiants par défaut :**
- **Username :** `admin`
- **Password :** `admin123`

⚠️ **Changez ce mot de passe après la première connexion !**

---

## 📱 ÉTAPE 6 : Partager avec Votre Équipe

### Si vous avez utilisé `lancer_en_ligne.py` :

1. **Copiez l'URL** qui s'affiche (ex: `https://abc123.ngrok.io`)
2. **Partagez-la** avec votre équipe par email/SMS/WhatsApp
3. **Ils peuvent se connecter** depuis n'importe où !

### Si vous utilisez en local seulement :

Consultez le guide `ACCES_RESEAU.md` pour permettre l'accès depuis d'autres PC du réseau local.

---

## 🎬 Résumé Visuel Complet

```
1. GitHub → Télécharger ZIP
              ↓
2. Extraire le ZIP sur votre PC (C:\TuberSYS3.0)
              ↓
3. Ouvrir Terminal/PowerShell
              ↓
4. cd C:\TuberSYS3.0
              ↓
5. pip install -r requirements.txt
              ↓
6. python lancer_en_ligne.py
              ↓
7. Copier l'URL publique
              ↓
8. Partager avec l'équipe !
```

---

## ❓ Résolution de Problèmes

### "python: command not found"
→ Python n'est pas installé ou pas dans le PATH
→ Essayez `python3` au lieu de `python`
→ Réinstallez Python en cochant "Add to PATH"

### "pip: command not found"
→ Essayez `pip3` au lieu de `pip`
→ Ou utilisez : `python -m pip install -r requirements.txt`

### "No such file or directory"
→ Vous n'êtes pas dans le bon dossier
→ Utilisez `cd` pour aller dans le dossier TuberSYS3.0
→ Sur Windows : `cd C:\TuberSYS3.0`
→ Sur Mac/Linux : `cd ~/TuberSYS3.0`

### "Permission denied"
→ Sur Linux/Mac, ajoutez `sudo` devant la commande pip
→ Ou utilisez un environnement virtuel

### Le fichier ZIP ne se décompresse pas
→ Sur Windows : Clic droit > "Extraire tout"
→ Sur Mac : Double-clic
→ Sur Linux : `unzip fichier.zip`

---

## 🎯 Checklist d'Installation

- [ ] Python 3.8+ installé et dans le PATH
- [ ] Projet téléchargé depuis GitHub
- [ ] Fichier ZIP extrait (si méthode ZIP)
- [ ] Terminal ouvert dans le dossier TuberSYS3.0
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Application lancée (`python lancer_en_ligne.py`)
- [ ] URL publique obtenue
- [ ] Connexion réussie avec admin/admin123
- [ ] Mot de passe changé

---

## 💡 Astuces

### Ouvrir le Terminal Directement dans le Bon Dossier

**Windows :**
1. Ouvrez l'Explorateur de fichiers
2. Allez dans `C:\TuberSYS3.0`
3. Dans la barre d'adresse, tapez `powershell` et Entrée
4. Le terminal s'ouvre déjà dans le bon dossier !

**Mac :**
1. Ouvrez Finder
2. Allez dans le dossier TuberSYS3.0
3. Clic droit > Services > "Nouveau terminal au dossier"

**Linux :**
1. Ouvrez le gestionnaire de fichiers
2. Allez dans le dossier TuberSYS3.0
3. Clic droit > "Ouvrir dans un terminal"

---

## 🆘 Besoin d'Aide ?

Si vous êtes bloqué, vérifiez :

1. **Python est installé :** `python --version`
2. **Vous êtes dans le bon dossier :** `pwd` (Mac/Linux) ou `cd` (Windows)
3. **Le fichier existe :** `ls lancer_en_ligne.py` (Mac/Linux) ou `dir lancer_en_ligne.py` (Windows)

---

## 🎉 Félicitations !

Une fois toutes ces étapes complétées, votre ERP TuberSYS 3.0 est opérationnel !

**Profitez de votre ERP ultra complet !** 🚀

---

**Version :** 3.0
**Date :** 2026
**Support :** Consultez README.md pour plus d'informations
