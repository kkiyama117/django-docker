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
$ docker-compose build
$ docker-compose up
```
