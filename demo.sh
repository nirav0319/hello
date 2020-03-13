#!/bin/bash
sudo  apt-get update
sudo apt-get install nginx
sudo apt-get install supervisor
sudo pip3 install gunicorn 
sudo cp ~/Desktop/gunicorn.conf  /etc/supervisor/conf.d/gunicorn.conf
cd /etc/supervisor/conf.d
sudo mkdir  /var/log/gunicorn
cd
cd Desktop
sudo supervisorctl reread
sudo supervisorctl update
cd /etc/nginx/sites-available
sudo cp ~/Desktop/django.conf  /etc/nginx/sites-available/django.conf
sudo ln django.conf /etc/nginx/sites-enabled
cd
cd Desktop
sudo nginx -t
sudo service nginx reload
sudo service nginx restart
 


