#!/bin/bash
# Script sends a JSON post request and displays body of response
curl -s -X POST -H "Content-Type: application/json" -d "@$2" $1
