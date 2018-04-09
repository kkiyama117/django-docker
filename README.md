# myHP
## You need

- docker
- docker-compose
- python
- django

### setting
- django - settings.py
  - `STATIC_ROOT = "/static/"`
  - `STATIC_URL = "/static/"`

## Usage
### initializing

```bash
# development server
cd django
rm -r mainHP
django-admin startproject mainHP
```

### Running

```bash
# development server
cd django/mainHP
python manage.py runserver
```

```bash
# production server test in local with docker
mkdir django/static
$ docker-compose -f docker-compose.dev.yml build
$ docker-compose -f docker-compose.dev.yml up

# if you want to run this on backbround
$ docker-compose -f docker-compose.dev.yml up -d

# run shell command
$ docker-compose -f docker-compose.dev.yml run web /bin/bash
```


```bash
# production server with docker in project root on remote server
mkdir django/static
$ docker-compose build
$ docker-compose up -d

# run shell command
$ docker-compose run web /bin/bash
```
