# JobBoardBackend
# Job Board Backend (ProDev BE)

A Django + PostgreSQL backend for a Job Board platform.

## Features
- JWT Authentication (Admin & User roles)
- Job & Category CRUD APIs
- Job Applications with role-based access
- Optimized job search & filtering
- Swagger API docs at `/api/docs`

## Tech Stack
- Django REST Framework
- PostgreSQL
- JWT (djangorestframework-simplejwt)
- Swagger (drf-yasg)

## Setup
```bash
git clone <repo>
cd jobboard-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
