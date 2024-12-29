This file documents the architectural decisions, rationale, and reasoning behind the configuration and choices made in the Foodie project. It serves as a reference for future enhancements, onboarding, or deeper understanding of the system’s design.

## Overview of Architectural Choices

### Why Django?
**Rationale:**  
Django is a robust and well-established Python web framework that simplifies rapid development and promotes best practices. It includes batteries for authentication, admin interface, ORM for database interactions, and a structured approach to project organization.

### Why Gunicorn?
**Rationale:**  
Gunicorn is a production-grade WSGI HTTP server that is commonly used with Django. Running Django behind Gunicorn is a standard best practice, as it allows for better scalability and load handling than Django’s built-in development server.

### Why Nginx?
**Rationale:**  
Nginx acts as a reverse proxy, handling SSL termination (in a real production scenario), static file serving, and request routing. It’s more performant and secure than directly exposing the Gunicorn server to the public internet.

### Why PostgreSQL?
**Rationale:**  
PostgreSQL is a reliable, production-grade relational database. It’s widely supported, and Django works seamlessly with it. Its rich feature set and compliance with SQL standards make it ideal for enterprise-level apps.

### Why Redis?
**Rationale:**  
Redis is chosen for caching and potentially for session management. It helps offload repetitive database queries and speeds up page loads, simulating a more production-realistic environment.

### Why Docker & Docker Compose?
**Rationale:**  
Containerization ensures reproducible builds and consistent environments across development, staging, and production. Docker Compose streamlines local development by orchestrating multiple services easily. This approach is a precursor to Kubernetes deployments.

### Why Prometheus & Grafana?
**Rationale:**  
Observability is a key aspect of production-ready systems. Prometheus scrapes metrics from the application and related services, while Grafana provides a friendly interface to visualize and analyze these metrics. Including them demonstrates knowledge in modern monitoring and alerting practices.

## Development vs. Production Settings

### Separate Settings Files
- **development.py:**  
  Designed for local use with `DEBUG=True`, permissive `ALLOWED_HOSTS`, and direct environment variable usage. No strict security or performance optimizations, but easy to iterate.
  
- **production.py:**  
  Geared towards a real-world environment, with `DEBUG=False`, stricter security settings (HSTS, secure cookies), and configurable `ALLOWED_HOSTS`. In a true production environment, secrets would be managed more securely (e.g., through Docker secrets or Vault).

### Environment Variables
Storing configuration in `.env` prevents hardcoding secrets and sensitive data. In real production, consider secrets managers, CI/CD variable stores, or environment injection at runtime. For demonstration, `.env` shows the concept without implementing full production-grade secret management.

## Dockerization

### Docker Compose
The docker compose files are divided into 3 parts docker-compose.yml, docker-compose.dev.yml and docker-compose.prod.yml. docker-compose.dev.yml is used to add service adminer which is a phpmyadmin style interface to manage and view your database. Use this only for local development. docker-compose.prod.yml is used to add service redis which is used for caching. Use this only for production. add the docker-compose.prod.yml and .env in .gitignore to ensure security.

**Command for development:** docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
**Command for production:** docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

### Development environment in Django Server:
Used the Django server for local development as any changes made will be updated in real time
- **Run Django Server:** python manage.py runserver
- **Run Adminer:** http://localhost:8080

### Production environment using NGINX reverse proxy and Gunicorn:
Used the Gunicorn server for production as it is more efficient, has better scalability and load handling. No need to use the 'python manage.py runserver' here as Nginx automatically starts the server.


## CI/CD Integration

### GitHub Actions
A continuous integration workflow is included in `.github/workflows/ci.yml`. It:
- Runs on every commit and PR.
- Checks code formatting (Black), linting (Flake8), and runs the test suite.
- This ensures code quality and stability are maintained and provides a foundation to add container scanning or automated deployments in the future.

## Observability and Metrics

- **Django-Prometheus:**  
  The `django-prometheus` package integrates Prometheus metrics into the Django application. Exporting metrics at `/metrics/` allows Prometheus to scrape and store performance, request rate, and error metrics.
  
- **Grafana Dashboards:**  
  With Grafana connected to Prometheus, custom dashboards can visualize key metrics. Although not fully configured here, it sets the stage for adding alerts, custom panels, and performance metrics to simulate a real production scenario.

## Logging and Tracing

- **Logging:**  
  Basic logging is configured in `base.py`, and production logging outputs to a file. This simulates a production environment where logs are often harvested by centralized logging systems.
  
- **Extensions:**  
  In a real environment, logs could be shipped to ELK/EFK stacks or cloud-based log management solutions. Tracing tools (like Jaeger) could be integrated for deeper request-level insights.

## SSL and Security Considerations

- **Nginx SSL Termination:**  
  Currently, SSL termination is not implemented. The structure allows it by mounting certificates into Nginx. For a real production scenario, configure `listen 443 ssl;` and provide TLS certificates (e.g., via Let’s Encrypt).

- **Security Headers:**  
  Nginx and Django can be configured to add strict security headers. The environment supports these adjustments, showing awareness of security best practices even if not fully implemented for a demo.

## Future Enhancements and Directions

- **Kubernetes Deployment:**  
  The project’s Docker-based design paves the way for Kubernetes manifests. Concepts like readiness/liveness probes, secrets, ConfigMaps, and Ingress controllers align well with the current architecture.

- **Celery and Background Tasks:**  
  Adding Celery with Redis for task queues could simulate asynchronous workloads typical in complex applications (e.g., sending newsletters, generating reports).

- **Load Testing and Performance Tuning:**  
  Tools like Locust or k6 could be integrated to highlight how the system scales and how caching and the database respond under load.

- **Additional Security and Compliance:**  
  Consider SAST/DAST tools, container scanning (Trivy), dependency scanning (Dependabot), and strict CSP rules to align with production security standards.

## Conclusion

This NOTES.md file provides insight into the thought process behind the architecture and technology choices. While not every aspect of a true production environment is fully realized, the project demonstrates readiness, scalability, observability, and code quality best practices that are hallmarks of professional production systems.