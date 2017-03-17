from pywebdeb:latest

WORKDIR /app

ADD requirements.txt /app/requirements.txt
ADD /so_server/app.py /app/app.py
ADD /so_server/nginx-site /app/default
ADD /so_server/uwsgi.ini /app/uwsgi.ini
RUN pip3 install -r requirements.txt

EXPOSE 80
RUN cp ./default /etc/nginx/sites-available/default
CMD uwsgi --ini uwsgi.ini & service nginx start & /bin/bash

