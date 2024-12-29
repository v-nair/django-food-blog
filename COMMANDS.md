## Docker Commands

### Comman Commands
```bash
docker compose build # builds the container
docker compose up -d # starts the container; use -d to run in background; (avoid logs)
docker compose up [container] -d # starts the specific container
docker ps # view the status of all containers; check if they are active and their health status
docker compose down # stops all the container
docker compose stop [container] # stops the specific container
docker logs [container] # see the logs of the specif container
docker exec -it [container_id] bash # enter into the bash of the specific container
```

### Making certificates
```bash
mkdir -p nginx/certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout nginx/certs/foodie.key \
    -out nginx/certs/foodie.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/OU=OrgUnit/CN=localhost"
```

## Django Commands
To run django commands you will need to enter into the django container.
```bash
docker compose stop web # only for development; stops the reverse proxy 
docker-compose run --rm --service-ports web python manage.py runserver 0.0.0.0:8000
```
or
```bash
docker exec -it [container_id] bash
```
Then you can run the following commands:

### create a new project
```bash
django-admin startproject [project_name]
```

### while using django server
```bash
python manage.py runserver 0.0.0.0:8000 # to start django server ; not required if running Gunicorn (production)
python3 manage.py startapp [app] # to create app section in django
```

### creating tables in database
```bash
python3 manage.py makemigrations [app] # to make migrations
python3 manage.py sqlmigrate [app] {migration no} # to get sql migration
python3 manage.py migrate # to migrate database
```

### creates the admin user for current django project
```bash
python3 manage.py createsuperuser # to create superuser
```

### accessing and managing tables
```bash
python3 manage.py shell # to start db shell
```