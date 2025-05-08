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

## DJANGO Commands - Local Development
To run django commands you will need to enter into the django container.
```bash
docker compose stop web # only for development; stops the reverse proxy 
docker-compose run --rm --service-ports web python3 manage.py runserver 0.0.0.0:8000
```
or
```bash
docker exec -it [container_id] bash
```
Then you can run the following commands:

## DJANGO Commands

django-admin startproject [project name]

python3 manage.py migrate # to create the default tables required in the INSTALLED_APPS

python3 manage.py startapp [app name]


python3 manage.py makemigrations [app name] # migrate tables
python3 manage.py migrate









# Queries
INSERT INTO "recipes_tag" ("id", "name") VALUES
(1,	'Instant Pot'),
(2,	'Chicken Breast'),
(3,	'Indian'),
(4,	'Japanese'),
(5,	'Shrimp'),
(6,	'Baking');


INSERT INTO "auth_user" ("id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES
(1,	'12345',	NULL,	'1',	'varsha',	'Varsha',	'Nair',	'varshanair.personal@gmail.com',	'1',	'1',	'2025-05-04 18:39:08.782105+00');


INSERT INTO "recipes_recipe" ("id", "title", "image", "description", "cooking_time", "servings", "created_at", "updated_at", "author_id") VALUES
(1,	'Ebi Fry (Japanese Fried Shrimp)',	'images/hot-cross-buns.png',	'Succulent jumbo prawns coated with panko breadcrumbs and fried till golden brown, this crunchy Japanese fried shrimp called Ebi Fry (Ebi Furai) is a popular Western-style (yoshoku) dish in Japan. Enjoy it with tartar sauce or tonkatsu sauce!',	75,	4,	'2025-05-04 18:40:03.435976+00',	'2025-05-04 18:40:03.435976+00',	1),
(2,	'Hot Cross Buns',	'images/hot-ebi-fry.png',	'These hot cross buns studded with plump dried cherries and luscious melty chunks of white chocolate are incredibly soft, fluffy, and delicious.',	165,	4,	'2025-05-04 18:44:49.644169+00',	'2025-05-04 18:44:49.644169+00',	1),
(3,	'Butter Chicken',	'images/butter-chicken.png',	'Instant Pot butter chicken is savory and saucy and perfect with rice and naan.',	30,	4,	'2025-05-04 18:46:25.20855+00',	'2025-05-04 18:46:25.20855+00',	1);


INSERT INTO "recipes_featured" ("id", "title", "image", "subtitle", "created_at", "updated_at", "recipe_id_id") VALUES
(1,	'How to make Ebi Fry',	'images/hot-cross-buns.png',	'Succulent jumbo prawns coated with panko breadcrumbs and fried till golden brown',	'2025-05-04 18:47:24.425472+00',	'2025-05-04 18:47:24.425472+00',	1),
(2,	'Hot Cross Buns',	'images/hot-cross-buns.png',	'These hot cross buns studded with plump dried cherries and luscious melty chunks of white chocolate',	'2025-05-04 18:48:09.283072+00',	'2025-05-04 18:48:09.283072+00',	2),
(3,	'Instant Pot Butter Chicken',	'images/butter-chicken.png',	'Instant Pot butter chicken is savory and saucy and perfect with rice and naan.',	'2025-05-04 18:48:42.813109+00',	'2025-05-04 18:48:42.813109+00',	3);


INSERT INTO "recipes_recipe_tags" ("id", "recipe_id", "tag_id") VALUES
(1,	1,	4),
(2,	1,	5),
(3,	2,	6),
(4,	3,	1),
(5,	3,	2),
(6,	3,	3);


