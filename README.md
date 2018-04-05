# myHP
## You need
- docker
- docker-compose

## Usage
```bash
# development server
cd docker/django/mainHP
# if it is your first run
# python manage.py makemigrations
# python manage.py migrate
# python manage.py collectstatic
python manage.py runserver
```

```bash
# production server with docker
cd mainHP
$ docker-compose build
$ docker-compose up
# run shell command
# $ docker-compose run web /bin/bash
```
