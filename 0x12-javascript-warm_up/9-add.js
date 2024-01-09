#!/usr/bin/node

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

const [,, arg1, arg2] = process.argv;

add(arg1, arg2);
