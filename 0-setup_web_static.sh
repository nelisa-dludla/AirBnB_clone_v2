#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

if [ ! -e /etc/nginx ]; then
	sudo apt update
	sudo apt install nginx -y
fi

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

html_content="<html>
	<head></head>
	<body>
		<h1>Holberton School</h1>
	</body>
</html>
" 

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

config_content="server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.nginx-debian.html;

	server_name _;
	add_header X-Served-By \$hostname;
	
	location /hbnb_static {
		alias /data/web_static/current;
	}

	location / {
		try_files \$uri \$uri/ =404;
	}
}
"

echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo service nginx restart
