#!/usr/bin/node

const request = require('request');

const [,, arg] = process.argv;

const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18';

request(arg, (error, response, body) => {
  if (error == null) {
    const film = JSON.parse(body);

    let filmCount = 0;

    film.results.forEach((film) => {
      if (film.characters.includes(characterUrl)) {
        filmCount++;
      }
    });
    console.log(filmCount);
  }
});
