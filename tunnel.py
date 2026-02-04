#!/usr/bin/env python3
"""
Script automatique pour mettre TuberSYS 3.0 en ligne
Utilise pyngrok pour créer un tunnel HTTPS gratuit
"""

import subprocess
import sys
import time
import os

def install_pyngrok():
    """Installer pyngrok si nécessaire"""
    try:
        import pyngrok
        print("✅ pyngrok est déjà installé")
    except ImportError:
        print("📦 Installation de pyngrok...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pyngrok"])
        print("✅ pyngrok installé avec succès")

def main():
    print("╔════════════════════════════════════════════════════╗")
    print("║   TuberSYS 3.0 - Mise en Ligne Automatique       ║")
    print("╚════════════════════════════════════════════════════╝")
    print("")

    # Installer pyngrok
    install_pyngrok()

    # Maintenant on peut l'importer
    from pyngrok import ngrok, conf

    # Configurer le port
    port = 5000

    print(f"🚀 Création du tunnel HTTPS pour le port {port}...")
    print("")

    try:
        # Créer le tunnel
        public_url = ngrok.connect(port, bind_tls=True)

        print("════════════════════════════════════════════════════")
        print("✅ VOTRE ERP EST EN LIGNE !")
        print("════════════════════════════════════════════════════")
        print("")
        print(f"🌐 URL Publique : {public_url}")
        print("")
        print("🔑 Connexion :")
        print("   Username: admin")
        print("   Password: admin123")
        print("")
        print("📱 Interface de monitoring : http://localhost:4040")
        print("")
        print("⚠️  IMPORTANT : Changez le mot de passe admin après connexion !")
        print("")
        print("Pour arrêter, appuyez sur Ctrl+C")
        print("════════════════════════════════════════════════════")
        print("")

        # Garder le tunnel actif
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👋 Arrêt du tunnel...")
            ngrok.kill()
            print("✅ Tunnel fermé")

    except Exception as e:
        print(f"❌ Erreur : {e}")
        print("")
        print("💡 Assurez-vous que :")
        print("   1. L'application Flask est lancée (python3 app.py)")
        print("   2. Le port 5000 est disponible")
        print("   3. Vous avez une connexion Internet")
        sys.exit(1)

if __name__ == "__main__":
    main()
