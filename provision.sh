#!/bin/bash

############
# packages #
############

sudo aptitude update
sudo aptitude install -y virtualenvwrapper python-dev

##############
# virtualenv #
##############

source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

# Create virtualenv
if [ ! -e ~/.virtualenvs/djregistry ]; then
    mkvirtualenv djregistry
fi

echo "cd /vagrant" > ~/.virtualenvs/djregistry/bin/postactivate

workon djregistry

if [ ! -e ~/.pip ]; then
    mkdir ~/.pip
fi

pip install requirements-dev.txt
