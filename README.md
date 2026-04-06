# Mini Projet Django + Next.js

Une application full-stack pour gérer les transactions avec **Django REST Framework** (backend) et **Next.js** (frontend).

## 🚀 Démarrage rapide

### Prérequis
- **Python 3.10+**
- **Node.js 18+**
- **Git**

---

## 📋 Installation

### 1️⃣ Cloner le repo
```bash
git clone https://github.com/TheRealBerete/Mini-projet-django.git
cd Mini-projet-django
```

### 2️⃣ Configurer le Backend (Django)

#### Activer le virtualenv
```bash
cd backend

# Sur Windows (PowerShell)
.\env\Scripts\activate

# Sur macOS/Linux
source env/bin/activate
```

#### Installer les dépendances
```bash
pip install -r requirements.txt
```

#### Lancer le serveur Django
```bash
python manage.py runserver 8000
```

✅ Backend disponible sur : **http://localhost:8000/api/**

---

### 3️⃣ Configurer le Frontend (Next.js)

#### Dans un nouveau terminal, accéder au dossier frontend
```bash
cd frontend
```

#### Installer les dépendances
```bash
npm install
```

#### Lancer le serveur de développement
```bash
npm run dev
```

✅ Frontend disponible sur : **http://localhost:3000** (ou **3001** si port occupé)

---

## 🎯 Utilisation

1. Ouvrez le frontend : **http://localhost:3000**
2. Cliquez sur "Ajouter Transaction" pour créer une nouvelle transaction
3. Remplissez les champs : **Texte**, **Description**, **Montant**
4. Consultez la liste des transactions en temps réel
5. Supprimez une transaction avec le bouton "Supprimer"

---

## 📂 Structure du projet

```
Mini-projet-django/
├── backend/                 # API Django + DRF
│   ├── api/                 # App principale
│   │   ├── models.py        # Modèle Transaction
│   │   ├── serializers.py   # Sérialisation REST
│   │   ├── views.py         # Endpoints API
│   │   └── urls.py          # Routage API
│   ├── backend/
│   │   ├── settings.py      # Configuration Django
│   │   ├── urls.py          # Routage principal
│   │   └── wsgi.py
│   ├── env/                 # Virtualenv (ignoré par Git)
│   ├── manage.py
│   └── db.sqlite3
│
├── frontend/                # UI Next.js
│   ├── app/
│   │   ├── page.tsx         # Page principale (formulaire + liste)
│   │   ├── layout.tsx       # Layout avec Toaster
│   │   ├── api.ts           # Client Axios
│   │   └── globals.css      # Styles Tailwind
│   ├── package.json
│   └── .env.local           # Config API URL (ignoré par Git)
│
├── .gitignore               # Exclusions Git
└── README.md
```

---

## 🔧 Configuration

### Variables d'environnement Frontend

Créer `frontend/.env.local` :
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/
```

### Endpoints API

- **GET/POST** `/api/transactions/` - Lister et créer des transactions
- **GET/DELETE/PUT** `/api/transactions/<uuid:id>/` - Détail, supprimer, modifier

---

## 🛠 Tech Stack

### Backend
- Python 3.x
- Django 6.0.3
- Django REST Framework 3.17
- django-cors-headers 4.9

### Frontend
- Next.js 16.2.2
- TypeScript
- Tailwind CSS
- Axios
- React Hot Toast

---

## 📝 Dépannage

### Backend : "ModuleNotFoundError: No module named 'django'"
→ Oubli d'activer le virtualenv
```bash
.\env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux
```

### Frontend : "Network Error"
→ Backend non lancé ou API URL incorrecte
- Vérifier que Django tourne sur `http://localhost:8000`
- Vérifier `.env.local` : `NEXT_PUBLIC_API_URL`

### Port 3000 déjà utilisé
→ Le serveur Next.js utilisera le port **3001** automatiquement

---

## 📦 Production

Pour déployer en production :

**Backend :**
```bash
pip install gunicorn
gunicorn backend.wsgi
```

**Frontend :**
```bash
npm run build
npm start
```

---

## 👤 Auteur

**TheRealBerete** - [GitHub](https://github.com/TheRealBerete)

---

## 📄 License

Libre d'utilisation.
