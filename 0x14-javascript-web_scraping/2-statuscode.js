#!/usr/bin/node

const request = require('request');

const [,, arg] = process.argv;

request(arg, (error, response) => {
  if (error == null) {
    console.log('code: ', response.statusCode);
  }
});
