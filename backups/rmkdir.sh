#!/bin/bash

# Replace with your server's IP address or hostname
USER_SERVER=$1

# Replace with the desired directory path
DIRECTORY_PATH=$2
OPT=$3

# Use SSH to execute the mkdir command on the remote server
ssh ${USER_SERVER} "mkdir ${OPT} ${DIRECTORY_PATH}"