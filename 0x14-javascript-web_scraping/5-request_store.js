#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const [,, url, path] = process.argv;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const content = body;

  fs.writeFile(path, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
