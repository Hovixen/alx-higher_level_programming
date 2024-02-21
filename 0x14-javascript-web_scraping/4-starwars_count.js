#!/usr/bin/node

const request = require('request');

const [,, arg] = process.argv;

const characterId = 18;

request(arg, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body).results;

  let filmCount = 0;

  film.forEach((film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      filmCount++;
    }
  });
  console.log(`${filmCount}`);
});
