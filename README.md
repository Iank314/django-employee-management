# Employee Management System – Django Internship Project

A full‑stack Django REST application that manages employees, departments, attendance, and performance, complete with JWT‑secured APIs, Swagger docs, database seeding, optional Chart.js dashboards, and Docker‑first deployment.

---

## ✨ Features

| Area       | Highlights                                                                      |
| ---------- | ------------------------------------------------------------------------------- |
| **Models** | Employee · Department · Attendance · Performance (relational, PostgreSQL‑ready) |
| **APIs**   | CRUD for every model · pagination · filtering · ordering · search               |
| **Auth**   | Simple JWT (access + refresh) · DRF session login fallback                      |
| **Docs**   | Swagger UI at `/swagger/` with Bearer auth box                                  |
| **Dev UX** | Faker data seeding (`manage.py seed_data`)                                      |
| **Charts** | Optional Chart.js dashboard (`/charts/`)                                        |
| **Docker** | `docker-compose.yml` spins up `web` + `db` in one command                       |

---

## 🖥️ Local‑venv Quick Start

```bash
# 0  Clone & enter
$ git clone <your‑repo> && cd django-employee-management

# 1  Create & activate venv
$ python -m venv venv
$ ./venv/Scripts/Activate.ps1   # Windows PowerShell

# 2  Install deps
(venv)$ pip install -r requirements.txt

# 3  Configure .env (SQLite)  ➜ cp .env.example .env
SECRET_KEY=<random>
DATABASE_URL=sqlite:///db.sqlite3
DEBUG=True

# 4  Run DB migrations & seed fake data
(venv)$ python manage.py migrate
(venv)$ python manage.py seed_data

# 5  Run dev server
(venv)$ python manage.py runserver
# Swagger → http://127.0.0.1:8000/swagger/
```

---

## 🐳 Docker Quick Start

> **Prerequisites:** Docker Desktop & Docker Compose v2

```bash
# 1  (Optional) copy env vars tuned for Postgres
$ cp .env.example .env.docker
# edit .env.docker → DATABASE_URL=postgres://postgres:postgres@db:5432/employee_db

# 2  Build & run containers
$ docker compose up --build -d

# 3  Run migrations & seed from inside the web container
$ docker compose exec web python manage.py migrate
$ docker compose exec web python manage.py seed_data

# 4  Browse
http://localhost:8000/swagger/
```

> **Stop everything:** `docker compose down -v`

---

## 🔑 Authentication Flow (JWT)

1. **Obtain tokens**
   `POST /api/token/`  → `{"access": "…", "refresh": "…"}`
2. **Attach header to every request**
   `Authorization: Bearer <access>`
3. **Refresh** when access expires
   `POST /api/token/refresh/ {"refresh":"<refresh>"}`

Swagger → click **Authorize** → paste `Bearer <access>` in the Bearer box.

---

## 🗄️ Project Structure (key parts)

```
employee_project/         # Django settings package
├── settings.py
├── urls.py               # global routes & Swagger view
├── wsgi.py

employees/                # app – models, serializers, views, urls
│   └── management/commands/seed_data.py
attendance/
performance/

Dockerfile                # builds the web image
docker-compose.yml        # web + db stack
requirements.txt
.env.example              # starter env
README.md                 
```

---

## 📓 Common Commands

| Action            | Command                            |
| ----------------- | ---------------------------------- |
| Run tests         | `pytest -q`                        |
| Create superuser  | `python manage.py createsuperuser` |
| List migrations   | `python manage.py showmigrations`  |
| Generate JWT pair | `curl -X POST /api/token/ …`       |

---

## 🛠️ Troubleshooting

| Issue                           | Fix                                                                         |
| ------------------------------- | --------------------------------------------------------------------------- |
| **401 Unauthorized** in Swagger | Make sure Bearer token pasted, not expired. Refresh or get a new pair.      |
| `UnorderedObjectListWarning`    | Add `ordering = ["id"]` in `Meta` or `.order_by()` in queryset.             |
| Docker pull 401                 | `docker login` to Docker Hub or check corporate proxy.                      |
| `SECRET_KEY` env error          | Copy `.env.example` → `.env` and set `SECRET_KEY` before running manage.py. |

---


This internship project is provided for learning purposes at **Springer Capital**.  
