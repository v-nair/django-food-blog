#!/bin/sh

set -e

echo "Starting entrypoint.sh..."

# Determine if we're in production or development
if [ "$DJANGO_ENVIRONMENT" = "production" ]; then
    echo "Running in production mode."
else
    echo "Running in development mode."
fi

# Wait for the database to be ready
if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for PostgreSQL to be ready at $DATABASE_HOST:$DATABASE_PORT..."
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL is ready."
fi

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec "$@"