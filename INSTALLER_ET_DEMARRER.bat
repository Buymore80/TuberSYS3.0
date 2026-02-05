@echo off
chcp 65001 >nul
cls
echo ╔════════════════════════════════════════════════════╗
echo ║        TuberSYS 3.0 - Installation Facile         ║
echo ╚════════════════════════════════════════════════════╝
echo.

echo 📍 Configuration automatique...
echo.

REM Créer le dossier data
if not exist "data" mkdir data

REM Créer un fichier Python temporaire pour initialiser
(
echo import os
echo import sys
echo.
echo # Changer vers le répertoire du script
echo os.chdir(os.path.dirname(os.path.abspath(__file__^)^)^)
echo.
echo # Configurer les variables d'environnement
echo os.environ['SECRET_KEY'] = 'cle-secrete-ultra-complexe'
echo os.environ['DATABASE_PATH'] = os.path.join(os.getcwd(^), 'data', 'tubersys.db'^)
echo os.environ['FLASK_ENV'] = 'development'
echo.
echo print(f"📁 Base de données : {os.environ['DATABASE_PATH']}"^)
echo print(f"📂 Dossier actuel : {os.getcwd(^)}"^)
echo print("")
echo.
echo # Importer et initialiser
echo try:
echo     from app import init_db
echo     print("🔧 Initialisation de la base de données..."^)
echo     init_db(^)
echo     print("")
echo     print("════════════════════════════════════════════════════"^)
echo     print("✅ INSTALLATION RÉUSSIE !"^)
echo     print("════════════════════════════════════════════════════"^)
echo     print("")
echo except Exception as e:
echo     print(f"❌ Erreur : {e}"^)
echo     sys.exit(1^)
) > init_temp.py

python init_temp.py

if %ERRORLEVEL% EQU 0 (
    del init_temp.py
    echo.
    echo 🚀 Lancement de l'application...
    echo.
    echo 🔑 Identifiants de connexion :
    echo    Username : admin
    echo    Password : admin123
    echo.
    echo 🌐 Ouvrez votre navigateur sur :
    echo    http://localhost:5000
    echo.
    echo ════════════════════════════════════════════════════
    echo.

    REM Définir les variables d'environnement pour l'application
    set SECRET_KEY=cle-secrete-ultra-complexe
    set DATABASE_PATH=%CD%\data\tubersys.db
    set FLASK_ENV=development

    python app.py
) else (
    del init_temp.py
    echo.
    echo ❌ Erreur lors de l'installation
    echo.
    pause
)
