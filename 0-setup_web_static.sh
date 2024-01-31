#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

nginx_dir="/etc/nginx"
data_dir="/data/web_static"

if [ ! -e "$nginx_dir" ]; then
	apt update
	apt install nginx -y
fi

mkdir -p "$data_dir/releases/test"
mkdir -p "$data_dir/shared"

chown ubuntu:ubuntu /data

html_content="<html>
	<head></head>
	<body>
		<h1>Holberton School</h1>
	</body>
</html>
" 

echo "$html_content" > "$data_dir/releases/test/index.html"

ln -sf "$data_dir/releases/test" "$data_dir/current"

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

echo "$config_content" > /etc/nginx/sites-available/default

service nginx restart
