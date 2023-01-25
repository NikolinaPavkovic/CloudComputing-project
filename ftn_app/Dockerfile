FROM python:3.10

WORKDIR /app 

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app 

RUN pip install django-cors-headers

RUN groupadd -r nina && useradd -g nina nina

RUN chown -R nina:nina /app

USER nina

CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8081