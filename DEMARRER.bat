@echo off
chcp 65001 >nul
cls
echo ╔════════════════════════════════════════════════════╗
echo ║   TuberSYS 3.0 - Configuration Automatique       ║
echo ╚════════════════════════════════════════════════════╝
echo.

echo 📍 Répertoire actuel : %CD%
echo.

echo 📁 Création du dossier data...
if not exist "data" (
    mkdir data
    echo ✅ Dossier data créé
) else (
    echo ✅ Dossier data existe déjà
)
echo.

echo 📝 Création du fichier .env...
(
echo SECRET_KEY=votre-cle-secrete-ultra-complexe-a-changer
echo DATABASE_PATH=%CD%\data\tubersys.db
echo FLASK_ENV=development
) > .env
echo ✅ Fichier .env créé avec chemin absolu
echo    DATABASE_PATH=%CD%\data\tubersys.db
echo.

echo 🔧 Initialisation de la base de données...
python -c "from app import init_db; init_db()"
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ════════════════════════════════════════════════════
    echo ✅ CONFIGURATION TERMINÉE AVEC SUCCÈS !
    echo ════════════════════════════════════════════════════
    echo.
    echo 🚀 Lancement de l'application...
    echo.
    echo 🔑 Connexion :
    echo    Username: admin
    echo    Password: admin123
    echo.
    echo 🌐 Ouvrez votre navigateur sur : http://localhost:5000
    echo.
    echo ════════════════════════════════════════════════════
    echo.
    python app.py
) else (
    echo.
    echo ❌ Erreur lors de l'initialisation
    echo Vérifiez que Python et toutes les dépendances sont installés
    echo.
    pause
)
