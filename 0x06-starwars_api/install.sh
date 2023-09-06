#!/usr/bin/env bash
# install nodejs

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install semi-standard
sudo npm install semistandard --global

# Install request
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
