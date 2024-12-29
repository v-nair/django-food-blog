Here is a brief explanation of each key file and directory:

## Root Level:
    docker-compose.yml: Orchestrates all services (Postgres, Redis, Django, Nginx, Prometheus, Grafana) into a cohesive application stack.
    docker-compose.dev.yml: additional services for development server
    docker-compose.prod.yml: additional services for production server
    .env.example: example .env file
    .gitignore: for git ignore
    .env: Stores environment variables to keep secrets (like DB passwords) out of source code.
    NOTES.md: Documents the architecture decisions, project overview, and the rationale behind each step. Helpful for anyone reviewing the project.

## .github/workflows/ci.yml:
    GitHub Actions workflow file that automates the build, test, and deployment process for the project.

## nginx/sites-enabled/foodie:
    The Nginx configuration file. It routes incoming HTTP requests to your Django web service and serves static files. No Python code here, just server configuration.

## prometheus/
    prometheus.yml:
        The configuration for Prometheus, telling it which endpoints to scrape for metrics.
    nginx-prometheus/
        .htpasswd:
            The password file for the Nginx reverse proxy to Prometheus.
        default.conf:
            The Nginx configuration file for the reverse proxy to Prometheus.
        Dockerfile:
            The Dockerfile for the Nginx reverse proxy to Prometheus.

## web/ Directory:
    Dockerfile: Defines how to build the Docker image for the Django application. The multi-stage build ensures a lightweight final image.
    requirements.txt: Lists the Python dependencies (Django, Gunicorn, etc.) with fixed versions.
    manage.py: Django’s command-line utility for administrative tasks (migrations, running the dev server, creating superusers).
    entrypoint.sh: a file run in the above dockerfile
    static/: A directory to hold static files like CSS, images, and JS.
    foodie/: The main Django project.
        __init__.py: Makes foodie a Python package.
        wsgi.py: Entry point for WSGI-compatible web servers like Gunicorn to serve the Django application.
        urls.py: The main URL routing file for the project. It includes routes from apps.
        views.py: for django health checks
        logs/: Contains logs.
            foodie.log: Write logs
        settings/: Contains configuration files.
            base.py: Common settings shared by all environments.
            development.py: Development-specific settings (e.g., DEBUG=True).
            production.py: Production-specific settings (e.g., DEBUG=False, secure database credentials).
