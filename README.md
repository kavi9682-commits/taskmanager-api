# 🧩 Task Manager REST API

A secure and scalable **Task Management API** built using **Django REST Framework** with **JWT authentication** and **Swagger documentation**.

---

## 🚀 Features
- User Registration and Login with JWT
- CRUD operations for Task model
- Token-based authentication
- Secure access to user-specific data
- Interactive API documentation (Swagger + Redoc)
- Tested using Postman

---

## ⚙️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Authentication:** SimpleJWT
- **Documentation:** drf-yasg (Swagger / Redoc)
- **Database:** SQLite (dev)
- **Language:** Python 3.10+

---

## 🛠️ Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/taskmanager-api.git
cd taskmanager-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# source venv/bin/activate  (Mac/Linux)

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
