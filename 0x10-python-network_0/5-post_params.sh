#!/bin/bash
# Script sends a POST request to the passed Url, and displays the body of the respond
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
