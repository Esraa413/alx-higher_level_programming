#!/bin/bash
#Bash script that sends a DELETE request to the URL passed the first argument
curl -sX DELETE "$1"
