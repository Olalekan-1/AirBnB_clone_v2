#!/usr/bin/env bash
# setting up webserver for deployment

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html><head></head><body>Test Page</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

link_path="/data/web_static/current"
target_path="/data/web_static/releases/test"

# Remove the symbolic link if it exists
if [ -L "$link_path" ]; then
    sudo rm -r "$link_path"
fi
# Create or recreate the symbolic link
sudo ln -sf "$target_path" "$link_path"
# sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content=$(cat <<EOF
server {
    listen 80 default_server;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    add_header X-Served-By: $HOSTNAME always;
     location / {
        add_header X-Served-By $HOSTNAME always;
        alias /data/web_static/releases/test/;
        index index.html;
    }


}
EOF
)

echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0

