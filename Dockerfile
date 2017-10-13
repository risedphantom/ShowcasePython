FROM python:latest

MAINTAINER Anton Panov

# Install uWSGI
RUN pip install uwsgi

# Set up Nginx and Supervisor
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y nginx supervisor \
	&& rm -rf /var/lib/apt/lists/*

# Redirect output
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443

# Make NGINX run on the foreground and copy configs
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY /cert/anpanov.crt /etc/nginx/conf.d/
COPY /cert/anpanov.key /etc/nginx/conf.d/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY uwsgi.ini /etc/uwsgi/

# Install application
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD ["/usr/bin/supervisord"]