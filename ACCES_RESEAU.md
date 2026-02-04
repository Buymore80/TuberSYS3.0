# 🌐 Guide d'Accès Réseau - TuberSYS 3.0

## Accéder au programme depuis d'autres PC du même réseau

### 1️⃣ Sur l'ordinateur serveur (celui qui héberge l'application)

#### Trouver votre adresse IP locale

**Windows :**
```cmd
ipconfig
```
Cherchez "Adresse IPv4" (ex: `192.168.1.10`)

**Linux/Mac :**
```bash
ip addr show
# OU
ifconfig
```
Cherchez votre IP locale (ex: `192.168.1.10`)

#### Modifier app.py pour accepter les connexions réseau

Le fichier `app.py` est déjà configuré avec :
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

`host='0.0.0.0'` signifie que l'application accepte les connexions de n'importe quelle adresse IP.

#### Lancer l'application
```bash
./start.sh
# OU
python app.py
```

### 2️⃣ Sur les autres ordinateurs du réseau

Ouvrez un navigateur et allez sur :
```
http://ADRESSE_IP_DU_SERVEUR:5000
```

**Exemple :**
Si l'IP du serveur est `192.168.1.10`, allez sur :
```
http://192.168.1.10:5000
```

### 3️⃣ Configuration du Pare-feu

#### Windows
1. Ouvrir **Pare-feu Windows Defender**
2. Cliquer sur **Règles de trafic entrant**
3. Nouvelle règle > **Port**
4. TCP > Port spécifique : **5000**
5. Autoriser la connexion
6. Appliquer à tous les profils
7. Nommer : "TuberSYS 3.0"

#### Linux (Ubuntu/Debian)
```bash
sudo ufw allow 5000/tcp
sudo ufw reload
```

#### Mac
```bash
# Le pare-feu Mac autorise généralement les connexions locales par défaut
# Si problème, aller dans Préférences Système > Sécurité > Pare-feu
```

---

## 🔒 Sécurité Important

⚠️ **ATTENTION** : Cette configuration est sécurisée uniquement pour un **réseau local privé** (votre bureau/maison).

**NE PAS** ouvrir le port 5000 sur Internet sans :
1. Configurer HTTPS (certificat SSL)
2. Changer la SECRET_KEY
3. Désactiver le mode DEBUG
4. Configurer un serveur web professionnel (nginx + gunicorn)

---

## 🌍 Pour Accès Internet (Production)

Pour un accès depuis Internet, consultez le guide de déploiement complet.

### Solutions recommandées :
1. **PythonAnywhere** (gratuit, facile)
2. **Heroku** (gratuit avec limites)
3. **VPS + Nginx + Gunicorn** (professionnel)

---

## 💡 Astuce : Nom de Domaine Local

Pour éviter de taper l'IP, vous pouvez configurer un nom :

**Windows** - Modifier `C:\Windows\System32\drivers\etc\hosts` :
```
192.168.1.10    tubersys.local
```

**Linux/Mac** - Modifier `/etc/hosts` :
```
192.168.1.10    tubersys.local
```

Puis accédez via : `http://tubersys.local:5000`

---

## 📊 Vérifier les Connexions

Pour voir qui est connecté, surveillez les logs dans le terminal où l'application tourne.

---

## ❓ Problèmes Courants

### "Impossible de se connecter"
- Vérifiez que le serveur est bien lancé
- Vérifiez l'adresse IP (ping depuis l'autre PC)
- Vérifiez le pare-feu
- Essayez de ping : `ping 192.168.1.10`

### "ERR_CONNECTION_REFUSED"
- Le pare-feu bloque le port 5000
- L'application n'est pas lancée
- Mauvaise adresse IP

### Performance lente
- SQLite n'est pas optimal pour beaucoup d'utilisateurs simultanés
- Considérez PostgreSQL pour plus de 5 utilisateurs simultanés

---

**Bon travail !** 🎉
