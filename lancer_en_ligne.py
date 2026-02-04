#!/usr/bin/env python3
"""
Script ULTRA SIMPLE pour mettre TuberSYS 3.0 en ligne
Lance l'application ET crée le tunnel automatiquement
"""

import subprocess
import sys
import time
import os
import signal

# Processus globaux
flask_process = None
tunnel_process = None

def cleanup(signum=None, frame=None):
    """Nettoyer les processus à la sortie"""
    global flask_process, tunnel_process
    print("\n\n🛑 Arrêt en cours...")

    if tunnel_process:
        tunnel_process.terminate()
        print("✅ Tunnel fermé")

    if flask_process:
        flask_process.terminate()
        print("✅ Application arrêtée")

    print("\n👋 Au revoir !")
    sys.exit(0)

def install_pyngrok():
    """Installer pyngrok si nécessaire"""
    try:
        import pyngrok
        return True
    except ImportError:
        print("📦 Installation de pyngrok (une seule fois)...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pyngrok"],
                                stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            print("✅ pyngrok installé")
            return True
        except:
            print("❌ Impossible d'installer pyngrok")
            print("   Installez-le manuellement : pip install pyngrok")
            return False

def init_database():
    """Initialiser la base de données si nécessaire"""
    if not os.path.exists('data/tubersys.db'):
        print("🔧 Initialisation de la base de données...")
        try:
            from app import init_db
            init_db()
            print("✅ Base de données créée")
        except Exception as e:
            print(f"⚠️  Avertissement : {e}")

def main():
    global flask_process, tunnel_process

    print("╔════════════════════════════════════════════════════╗")
    print("║     TuberSYS 3.0 - Lancement Automatique         ║")
    print("║            TOUT-EN-UN (Gratuit)                   ║")
    print("╚════════════════════════════════════════════════════╝")
    print("")

    # Gérer Ctrl+C proprement
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    # Initialiser la base de données
    init_database()

    # Installer pyngrok
    if not install_pyngrok():
        sys.exit(1)

    # Importer après installation
    from pyngrok import ngrok

    print("🚀 Démarrage de l'application Flask...")

    # Lancer Flask en arrière-plan
    flask_process = subprocess.Popen(
        [sys.executable, "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Attendre que Flask démarre
    print("⏳ Attente du démarrage (5 secondes)...")
    time.sleep(5)

    # Vérifier que Flask tourne
    if flask_process.poll() is not None:
        print("❌ Erreur : L'application Flask n'a pas démarré")
        print("   Vérifiez les erreurs dans app.log")
        sys.exit(1)

    print("✅ Application Flask démarrée")
    print("")
    print("🌐 Création du tunnel HTTPS (gratuit)...")
    print("")

    try:
        # Créer le tunnel ngrok
        public_url = ngrok.connect(5000, bind_tls=True)

        print("════════════════════════════════════════════════════")
        print("✨ VOTRE ERP EST MAINTENANT EN LIGNE ! ✨")
        print("════════════════════════════════════════════════════")
        print("")
        print(f"🌍 URL Publique : {public_url}")
        print("")
        print("📋 Partagez cette URL avec votre équipe !")
        print("")
        print("🔑 Identifiants de Connexion :")
        print("   👤 Username : admin")
        print("   🔒 Password : admin123")
        print("")
        print("📊 Monitoring : http://localhost:4040")
        print("")
        print("⚠️  IMPORTANT : Changez le mot de passe après connexion !")
        print("")
        print("🛑 Pour arrêter : Appuyez sur Ctrl+C")
        print("════════════════════════════════════════════════════")
        print("")

        # Garder actif
        print("💡 Le tunnel est actif, votre ERP est accessible...")
        print("")

        try:
            # Attendre indéfiniment
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            cleanup()

    except Exception as e:
        print(f"❌ Erreur lors de la création du tunnel : {e}")
        print("")
        print("💡 Vérifiez votre connexion Internet")
        cleanup()
        sys.exit(1)

if __name__ == "__main__":
    # Changer vers le bon répertoire
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
