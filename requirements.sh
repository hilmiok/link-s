#!/bin/bash

uname -m > mim.txt

echo "system updating..."
apt-get update
apt-get upgrade

echo "install php and python3"
apt-get install php
apt-get install python3

echo "unzip archive"
unzip ngrok-i686.zip
unzip ngrok-x86_64

