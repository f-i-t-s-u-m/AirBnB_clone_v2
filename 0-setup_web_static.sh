#!/usr/bin/env bash
# init project

sudo apt-get -y install nginx
mkdir -p /data
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo 'Hello World!' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo bash -c 'sudo chown -hR ubuntu:ubuntu data'
str="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"
sudo sed -i "47s|.*|$str|" /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
