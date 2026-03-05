#!/bin/bash
set -e

# Optional: pass Docker image as first argument
IMAGE=${1:-theinnocent/steam_forum:latest}

echo "Deploying $IMAGE ..."

# 1️⃣ Stop old containers safely
docker-compose down || true

# 2️⃣ Pull latest images
docker-compose pull

# 3️⃣ Start services
docker-compose up -d --build

# 4️⃣ Run Django migrations
docker-compose exec web python manage.py migrate

# 5️⃣ Collect static files
docker-compose exec web python manage.py collectstatic --noinput

echo "Deployment finished!"

