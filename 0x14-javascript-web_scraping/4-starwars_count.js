#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const films = data.results;
  const filmsWithCharacter = films.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );
  console.log(filmsWithCharacter.length);
});
