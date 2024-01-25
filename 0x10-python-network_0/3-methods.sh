#!/bin/bash
# Script displays all HTTP methods that server will accept
curl -sI -X OPTIONS $1 | grep -i allow | sed 's/Allow: //i'
