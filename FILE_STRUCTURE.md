.
├── .github/
│   └── workflows/
│       └── ci.yml                          # CI/CD pipeline configuration
│
├── nginx/
│   ├── certs/
│   │   ├── foodie.crt                      # certificate : auto generated
│   │   └── foodie.key                      # secreate key : auto generated
│   └── sites-enabled/
│       └── foodie                          # Nginx configuration file
│
├── prometheus/
│   ├── nginx-prometheus/
│   │   ├── .htpasswd                       # The password file for the Nginx reverse proxy
│   │   ├── default.conf                    # configuration file for the reverse proxy
│   │   └── Dockerfile                      # Dockerfile for the Nginx reverse proxy
│   └── prometheus.yml                      # configuration for Prometheus
│
├── web/
│   ├── foodie/
│   │   ├── logs/
│   │   │   └── foodie.log                  # Log File
│   │   ├── settings/
│   │   │   ├── __init__.py                 # 
│   │   │   ├── base.py                     # Common settings shared by all environments
│   │   │   ├── development.py              # Development-specific settings
│   │   │   └── production.py               # Production-specific settings
│   │   ├── templates/
│   │   │   ├── base.html                   # Base File Structure
│   │   │   ├── index.html                  # Home Page Html
│   │   │   └── navbar.html                 # Base NavBar Structure
│   │   ├── tests/
│   │   │   ├── __init__.py                 # 
│   │   │   └── test_health.py              # Health Check Test
│   │   ├── __init__.py                     # 
│   │   ├── asgi.py                         # 
│   │   ├── urls.py                         # URL routing file
│   │   ├── utils.py                        # 
│   │   ├── views.py                        # for django health checks
│   │   └── wsgi.py                         # Entry point for WSGI-compatible web servers
│   │
│   ├── logs/
│   │   └── foodie.log                      # Log File
│   │
│   ├── accounts/
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   └── accounts/
│   │   │       ├── details.html            # View Blog post : Need to change design
│   │   │       ├── index.html
│   │   │       └── item-form.html          # Add Blog post : Need to change design
│   │   ├── __init__.py                     # 
│   │   ├── admin.py                        # 
│   │   ├── apps.py                         # 
│   │   ├── forms.py                        # 
│   │   ├── models.py                       # 
│   │   ├── signals.py                      # 
│   │   ├── tests.py                        # 
│   │   └── views.py                        # 
│   │
│   ├── recipes/
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   └── recipes/
│   │   │       ├── details.html            # View Blog post : Need to change design
│   │   │       ├── index.html
│   │   │       └── item-form.html          # Add Blog post : Need to change design
│   │   ├── __init__.py                     # 
│   │   ├── admin.py                        # 
│   │   ├── apps.py                         # 
│   │   ├── forms.py                        # 
│   │   ├── models.py                       # model files
│   │   ├── tests.py                        # 
│   │   ├── urls.py                         # URL routing file
│   │   └── views.py                        # 
│   │
│   ├── mediafiles/
│   │   ├── images/
│   │   │   ├── placeholder.png             # Default image for Post Image
│   │   │   └── profile.png                 # Default for Profile Image
│   │   └── profile_pictures/
│   │
│   ├── staticfiles/
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   │   └──     # List of All CSS files
│   │   │   ├── img/
│   │   │   │   └──     # List of All Images files
│   │   │   └── js/
│   │   │       └──     # List of All JS files
│   │   │
│   │   ├── bootstrap/                      # Bootstrap and Jquery
│   │   │   ├── bootstrap@5.3.3.bundle.min.js
│   │   │   ├── bootstrap@5.3.3.min.css
│   │   │   └── jquery-3.7.1.min.js
│   │   │
│   │   ├── common/
│   │   │   ├── css/
│   │   │   │   ├── media.css               # Responsive CSS
│   │   │   │   ├── rte_theme_default.css   # Rich Text Editor CSS
│   │   │   │   └── style.css               # Comman Style CSS
│   │   │   └── js/
│   │   │       ├── rte_all_plugins.js      # Rich Text Editor
│   │   │       └── rte.js                  # Rich Text Editor
│   │   │
│   │   ├── recipes/
│   │   │   ├── css/
│   │   │   │   └── # Empty for now
│   │   │   └── js/
│   │   │       └── index.js                # List of All JS files
│   │   │
│   │   └── health.html                     # For Health check
│   │
│   ├── Dockerfile                          # Docker configuration
│   ├── entrypoint.sh                       # Dependency for dockerfile : to check if DB works
│   ├── manage.py                           # To start the Django Application
│   └── requirements.txt                    # Python dependencies
├── .env                                    # Environment variables
├── .env.example                            # Environment Format example
├── .gitignore                              # Git ignore
├── architecture.png                        # Flow of Architecture
├── COMMANDS.md                             # Docker And Django Commands for referrence
├── docker-compose.dev.yml                  # Docker Compose configuration for Development only
├── docker-compose.yml                      # Docker Compose configuration
├── FILE_STRUCTURE.md                       # File Structure of the architecture
├── NOTES.md                                # Notes for Development Process
└── README.md                               # Read Me file

Here is a brief explanation of each key file and directory:

#    # Root Level:
    docker-compose.yml: Orchestrates all services (Postgres, Redis, Django, Nginx, Prometheus, Grafana) into a cohesive application stack.
    docker-compose.dev.yml: additional services for development server
    docker-compose.prod.yml: additional services for production server
    .env.example: example .env file
    .gitignore: for git ignore
    .env: Stores environment variables to keep secrets (like DB passwords) out of source code.
    NOTES.md: Documents the architecture decisions, project overview, and the rationale behind each step. Helpful for anyone reviewing the project.

#    # .github/workflows/ci.yml:
    GitHub Actions workflow file that automates the build, test, and deployment process for the project.

#    # nginx/sites-enabled/foodie:
    The Nginx configuration file. It routes incoming HTTP requests to your Django web service and serves static files. No Python code here, just server configuration.

#    # prometheus/
    prometheus.yml:
        The configuration for Prometheus, telling it which endpoints to scrape for metrics.
    nginx-prometheus/
        .htpasswd:
            The password file for the Nginx reverse proxy to Prometheus.
        default.conf:
            The Nginx configuration file for the reverse proxy to Prometheus.
        Dockerfile:
            The Dockerfile for the Nginx reverse proxy to Prometheus.

#    # web/ Directory:
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
