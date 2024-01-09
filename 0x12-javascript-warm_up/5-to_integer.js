#!/usr/bin/node

const [,, arg] = process.argv;

if (Number(arg)) {
  console.log('My number: ', parseInt(arg));
} else {
  console.log('Not a number');
}
