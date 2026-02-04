#!/bin/bash
# Alternative simple sans installation - Utilise Serveo (SSH tunnel)

echo "╔════════════════════════════════════════════════════╗"
echo "║   TuberSYS 3.0 - En Ligne SANS Installation      ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Vérifier la base de données
if [ ! -f "data/tubersys.db" ]; then
    echo "🔧 Initialisation de la base de données..."
    python3 -c "from app import init_db; init_db()"
fi

echo "🚀 Lancement de TuberSYS 3.0..."

# Lancer l'application en arrière-plan
python3 app.py > app.log 2>&1 &
APP_PID=$!

# Attendre que l'app démarre
echo "⏳ Démarrage de l'application..."
sleep 4

echo ""
echo "🌐 Création du tunnel SSH (Serveo)..."
echo ""
echo "════════════════════════════════════════════════════"
echo "✅ VOTRE ERP EST EN LIGNE !"
echo "════════════════════════════════════════════════════"
echo ""
echo "📱 L'URL publique va s'afficher ci-dessous..."
echo ""
echo "🔑 Connexion :"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "Pour arrêter, appuyez sur Ctrl+C"
echo "════════════════════════════════════════════════════"
echo ""

# Créer le tunnel SSH avec Serveo
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:5000 serveo.net

# Nettoyer à la sortie
trap "kill $APP_PID 2>/dev/null" EXIT
