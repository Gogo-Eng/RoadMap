#!/usr/bin/env bash
#  script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

cat <<EOF > /data/web_static/releases/test/index.html
<html>
	<head>
	</head>
    	<body>
		Holberton School
	</body>
</html>
EOF

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

data_symbolink="/data/web_static/current/"
nginx_config="/etc/nginx/sites-available/default"

sudo sed -i "/listen 80 default_server;/a \\
\\
	location /hbnb_static { \\
		alias $data_symbolink; \\
	}" $nginx_config

sudo ufw allow "Nginx HTTP"
sudo service nginx restart
exit 0  
