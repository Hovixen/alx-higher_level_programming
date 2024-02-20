#!/usr/bin/node

const fs = require('fs');

const [,, arg1, arg2] = process.argv;

fs.writeFile(arg1, arg2, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
