#!/bin/sh


#This shell is created to solve the "apt-get update" problem, in which it occurs a signature error.
sudo apt-get clean
sudo mv /var/lib/apt/lists /var/lib/apt/list.old
sudo mkdir -p /var/lib/apt/lists/partial
sudo apt-get clean
sudo apt-get update
