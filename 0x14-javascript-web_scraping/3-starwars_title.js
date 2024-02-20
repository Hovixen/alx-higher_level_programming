#!/usr/bin/node

const request = require('request');

const [,, arg] = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);

  console.log(film.title);
});
