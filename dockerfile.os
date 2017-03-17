FROM debian:latest
EXPOSE 80
RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        nginx \
		curl \
		man \
		make \
		uwsgi \
		uwsgi-plugin-python3

