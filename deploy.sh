#!/bin/bash
set -e

# Docker image passed as first argument
IMAGE=$1

echo "Deploying $IMAGE ..."

# Stop old container if exists
if [ "$(docker ps -q -f name=steam_django)" ]; then
    echo "Stopping old container..."
    docker stop steam_django
    docker rm steam_django
fi

# Run new container
docker run -d \
  --name steam_django \
  --env-file .env \
  -p 8000:8000 \
  $IMAGE

# Run Django migrations
docker exec steam_django python manage.py migrate

# Collect static files
docker exec steam_django python manage.py collectstatic --noinput

echo "Deployment finished!"

