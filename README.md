# StreamEngine-UI

Currently this repo contains a monolith django app comprising the app features of UI, Admin, and API. 
The plan is ultimately to separate it into those respective pieces, and leave this repo to be only for UI. 



## Deploy

There are essentially two parts right now, with a third (db) being worked on.

You have the docker-compose portion and the Nginx portion

### uWSGI config/dockerfile

Hot reload is turned on by default

to disable:
remove the param:

```--py-autoreload=1```

from

```CMD ["uwsgi", "--py-autoreload=1"]```

### Docker

Install docker and docker-compose

clone this repo and check directory names editing the docker compose file as necessary

then run ```docker-compose up --build -d```


### NGINX

Install Nginx to your server
then create ```ui.conf``` under ```/etc/nginx/sites-available```
copy the contents of my nginx.conf to ```ui.conf```
then run ```ln -s /etc/nginx/sites-available/ui.conf /etc/nginx/sites-enabled/```
Reload Nginx

### config
edit the ```ui.conf``` for domain and ssl


#### Reference
Nginx: https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04

Django over uwsgi: https://www.eidel.io/2017/07/10/dockerizing-django-uwsgi-postgres/

Dockerfile: https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/