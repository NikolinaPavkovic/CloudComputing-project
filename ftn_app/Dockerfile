FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install django-cors-headers

CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8081