# myHP
## You need

- docker
- docker-compose
- python
- django

## Usage
### initializing

```bash
# development server
cd django
django-admin startproject mainHP
```

### Running

```bash
# development server
cd django/mainHP
# if it is your first run
# python manage.py makemigrations
# python manage.py migrate
# python manage.py collectstatic
python manage.py runserver
```

```bash
# production server test in local with docker
mkdir django/static
$ docker-compose -f docker-compose.dev.yml build
$ docker-compose -f docker-compose.dev.yml up

# if you want to run this on backbround
$ docker-compose -f docker-compose.dev.yml up -d

# if it is your first run
$ docker-compose -f docker-compose.dev.yml run web python mainHP/manage.py makemigrations
$ docker-compose -f docker-compose.dev.yml run web python mainHP/manage.py migrate
$ docker-compose -f docker-compose.dev.yml run web python mainHP/manage.py collectstatic

# run shell command
$ docker-compose -f docker-compose.dev.yml run web /bin/bash
```


```bash
# production server with docker in project root on remote server
mkdir django/static
$ docker-compose build
$ docker-compose up -d

# if it is your first run
$ docker-compose run web python mainHP/manage.py makemigrations
$ docker-compose run web python mainHP/manage.py migrate
$ docker-compose run web python mainHP/manage.py collectstatic

# run shell command
$ docker-compose run web /bin/bash
```
