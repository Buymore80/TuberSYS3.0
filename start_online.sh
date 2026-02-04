#!/bin/bash
# Script pour mettre TuberSYS 3.0 en ligne immédiatement

echo "╔════════════════════════════════════════════════════╗"
echo "║   TuberSYS 3.0 - Mise en Ligne Immédiate         ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Vérifier si ngrok est installé
if ! command -v ngrok &> /dev/null; then
    echo "📥 Installation de ngrok..."

    # Détecter l'OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        wget -q https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
        tar xzf ngrok-v3-stable-linux-amd64.tgz
        sudo mv ngrok /usr/local/bin/
        rm ngrok-v3-stable-linux-amd64.tgz
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install ngrok
    else
        echo "❌ Téléchargez ngrok depuis: https://ngrok.com/download"
        echo "   Puis relancez ce script"
        exit 1
    fi
fi

echo "✅ ngrok est prêt"
echo ""

# Vérifier la base de données
if [ ! -f "data/tubersys.db" ]; then
    echo "🔧 Initialisation de la base de données..."
    python3 -c "from app import init_db; init_db()"
fi

echo "🚀 Lancement de TuberSYS 3.0..."
echo ""

# Lancer l'application en arrière-plan
python3 app.py > /dev/null 2>&1 &
APP_PID=$!

# Attendre que l'app démarre
sleep 3

echo "🌐 Création du tunnel ngrok..."
echo ""

# Lancer ngrok
ngrok http 5000 &
NGROK_PID=$!

echo ""
echo "════════════════════════════════════════════════════"
echo "✅ VOTRE ERP EST EN LIGNE !"
echo "════════════════════════════════════════════════════"
echo ""
echo "📱 Pour voir l'URL publique :"
echo "   Ouvrez http://localhost:4040 dans votre navigateur"
echo "   OU regardez dans la fenêtre ngrok ci-dessus"
echo ""
echo "🔑 Connexion :"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "Pour arrêter, appuyez sur Ctrl+C"
echo "════════════════════════════════════════════════════"
echo ""

# Attendre et nettoyer à la sortie
trap "kill $APP_PID $NGROK_PID 2>/dev/null" EXIT
wait
