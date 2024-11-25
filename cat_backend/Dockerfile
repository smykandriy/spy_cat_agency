FROM python:3.11

COPY ./server /opt/server
COPY manage.py /opt/

WORKDIR /opt/

RUN pip install -r server/requirements.txt

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000