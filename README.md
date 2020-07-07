# StreamEngine-UI

Currently this repo contains a monolith django app comprising the app features of UI, Admin, and API. 
The plan is ultimately to separate it into those respective pieces, and leave this repo to be only for UI. 



## Deploy

There are essentially two parts right now, with a third (db) being worked on.

You have the docker-compose portion and the Nginx portion

### Docker

Install docker and docker-compose

clone this repo and check directory names editing the docker compose file as necessary

then run ```docker-compose --build u -d```


### NGINX

Install Nginx to your server
then create ```ui.conf``` under ```/etc/nginx/sites-available```
copy the contents of my nginx.conf to ```ui.conf```
then run ```ln -s /etc/nginx/sites-available/ui.conf /etc/nginx/sites-enabled/```
Reload Nginx

### config
edit the ```ui.conf``` for domain and ssl
