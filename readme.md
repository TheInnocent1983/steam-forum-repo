## 🔗 Quick Links

[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github)](https://github.com/TheInnocent1983/steam-forum-repo)

[![Docker](https://img.shields.io/badge/Docker-Hub-2496ED?style=for-the-badge&logo=docker)](https://hub.docker.com/repository/docker/theinnocent_steam_forum)

[![YouTube](https://img.shields.io/badge/YouTube-Video-FF0000?style=for-the-badge&logo=youtube)](https://youtu.be/OAEHqOrv-Hg?si=1blE2f7F3INqhpgr)

[![Website IP](https://img.shields.io/badge/Website-20.174.18.69-blue?style=flat&logo=googlechrome&logoColor=white)](http://20.174.18.69/)

[![Website Azure](https://img.shields.io/badge/Website-20.174.18.69-blue?style=flat&logo=googlechrome&logoColor=white)](http://steam-forum.uaenorth.cloudapp.azure.com/)

---

## Features
- **User Authentication:** Sign up, log in, and logout functionality.
- **Forum Management:** Create, read, update, and delete game topics.
- **Commenting System:** Users can post and manage comments on specific games.
- **Admin Interface:** Full CRUD capabilities via Django Admin.
- **Containerized Environment:** Fully dockerized setup for consistent development.

# Steam Django Backend

Backend service built with **Django**, **PostgreSQL**, **Docker**, and **Nginx**.  
The application runs inside Docker containers orchestrated with Docker Compose.

---

## Local setup instructions

#### Clone the Repository
```bash
   git clone https://github.com/TheInnocent1983/steam-forum-repo.git
   cd steam-forum-repo
```

#### Configure Environment Variables
```bash
   touch .env  # or create it manually in VS Code

   # Django settings
   SECRET_KEY=r63-o+u_r5b8t&8&po_kj!wbod1znu-2%n3#u1($!w%mar5=yk5
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Database settings
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=steam_db
   DB_USER=steamuser
   DB_PASSWORD=steampass123
   DB_HOST=db
   DB_PORT=5432
```

#### Launch the Local Environment
``` bash
   docker compose up --build
```

## Tech Stack

- Django
- PostgreSQL
- Docker
- Docker Compose
- Nginx

---

## Deployment
To deploy to a production environment:
1. Ensure Docker and Docker Compose are installed on your server.
2. Clone the repository.
3. Configure your production `.env` file.
4. Run the deployment script:
   ```bash
   docker compose -f docker-compose.prod.yml up -d

## Project Structure

```text
.
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── settings.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── wsgi.cpython-311.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── deploy.sh
├── docker-compose.prod.yml
├── docker-compose.yml
├── Dockerfile
├── forum
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-311.pyc
│   │   ├── apps.cpython-311.pyc
│   │   ├── forms.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── models.cpython-311.pyc
│   │   ├── urls.cpython-311.pyc
│   │   └── views.cpython-311.pyc
│   ├── templates
│   │   ├── forum
│   │   │   ├── base.html
│   │   │   ├── comment_confirm_delete.html
│   │   │   ├── comment_edit.html
│   │   │   ├── game_confirm_delete.html
│   │   │   ├── game_create.html
│   │   │   ├── game_detail.html
│   │   │   ├── game_edit.html
│   │   │   ├── game_list.html
│   │   │   ├── partials
│   │   │   │   └── navbar.html
│   │   │   ├── topic_confirm_delete.html
│   │   │   ├── topic_create.html
│   │   │   └── topic_detail.html
│   │   └── registration
│   │       ├── login.html
│   │       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── funnychanges.txt
├── gunicorn.conf.py
├── manage.py
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── pytest.ini
├── readme.md
└── requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
# Django settings
SECRET_KEY=r63-o+u_r5b8t&8&po_kj!wbod1znu-2%n3#u1($!w%mar5=yk5
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_ENGINE=django.db.backends.postgresql
DB_NAME=steam_db
DB_USER=steamuser
DB_PASSWORD=steampass123
DB_HOST=db
DB_PORT=5432
```

---

## Docker Services

The project uses three services.

### Database

PostgreSQL database container.

```yaml
image: postgres:15-alpine
container_name: steam_postgres
```

### .gitignore

```.gitingore
.env
venv/
__pycache__/
*.pyc
db.sqlite3
```

### .flake8

```.flake8
[flake8]
exclude = 
    .git,
    __pycache__,
    migrations,
    .venv,
    env
max-line-length = 119
```

### 

### Web (Django)

Runs the Django application.

```yaml
container_name: steam_django
command: python manage.py runserver 0.0.0.0:8000
```

### Nginx

Acts as a reverse proxy and serves static/media files.

```yaml
container_name: steam_nginx
ports:
  - "80:80"
```

---

## Build Containers

```bash
docker compose build
```

---

## Start the Application

Start all services:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

---

## Run Migrations

Apply migrations:

```bash
docker compose exec web python manage.py migrate
```

Create migrations:

```bash
docker compose exec web python manage.py makemigrations
```

---

## Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

## Collect Static Files

```bash
docker compose exec web python manage.py collectstatic --noinput
```

---

## Access the Application

Main application:

```
http://localhost
```

Django admin panel:

```
http://localhost/admin
```

---

## View Logs

View logs for all services:

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

Logs for Django only:

```bash
docker compose logs -f web
```

---

## Stop Containers

Stop containers:

```bash
docker compose down
```

Stop containers and remove volumes:

```bash
docker compose down -v
```

---

## Rebuild Containers

If dependencies or Dockerfiles change:

```bash
docker compose build --no-cache
docker compose up
```

---

## Running Django Commands

Open Django shell:

```bash
docker compose exec web python manage.py shell
```

Run tests:

```bash
docker compose exec web python manage.py test
```

---

## Development Workflow

Typical workflow:

```bash
docker compose up -d
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

---

## Reset Database

To reset the database completely:

```bash
docker compose down -v
docker compose up
```
