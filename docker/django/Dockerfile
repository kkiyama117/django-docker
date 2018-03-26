FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD . /uwsgi

RUN mkdir -p /mainHP
RUN mkdir -p /static
ADD mainHP /mainHP
ADD static /static

WORKDIR /uwsgi
RUN pip install -r /uwsgi/requirements.in

WORKDIR /mainHP
RUN pip install -r /mainHP/requirements.in
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py collectstatic

WORKDIR /uwsgi
