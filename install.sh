#!/bin/bash



sudo mkdir /opt/tub

sudo cp ./info.json /opt/tub
sudo cp ./translate.py /opt/tub
sudo cp ./tub /opt/tub

export PATH="$PATH:/opt/tub"

echo install tub successful