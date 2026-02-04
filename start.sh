#!/bin/bash
# Script de démarrage de TuberSYS 3.0

echo "╔══════════════════════════════════════════════════╗"
echo "║        TuberSYS 3.0 - ERP Ultra Complet         ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Vérifier que Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

# Vérifier que les dépendances sont installées
if [ ! -d "venv" ]; then
    echo "📦 Installation des dépendances..."
    pip install -q -r requirements.txt
fi

# Vérifier que la base de données existe
if [ ! -f "data/tubersys.db" ]; then
    echo "🔧 Initialisation de la base de données..."
    python3 -c "from app import init_db; init_db()"
fi

echo ""
echo "🚀 Démarrage de TuberSYS 3.0..."
echo ""
echo "📝 Connexion par défaut:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "🌐 Accédez à l'application sur: http://localhost:5000"
echo ""
echo "Pour arrêter l'application, appuyez sur Ctrl+C"
echo "══════════════════════════════════════════════════"
echo ""

# Lancer l'application
python3 app.py
