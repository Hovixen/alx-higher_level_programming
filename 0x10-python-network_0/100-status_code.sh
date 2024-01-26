#!/bin/bash
# Script displays only the status code of a Url passed
curl -s -o /dev/null -w "%{http_code}" $1
