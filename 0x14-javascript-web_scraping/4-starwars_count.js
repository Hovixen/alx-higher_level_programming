#!/usr/bin/node

const request = require('request');

const [,, arg] = process.argv;

const characterId = 18;

request(arg, (error, response, body) => {
  if (error == null) {
    const film = JSON.parse(body);

    let filmCount = 0;

    film.results.forEach((filmRes) => {
      if (filmRes.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        filmCount++;
      }
    });
    console.log(filmCount);
  }
});
