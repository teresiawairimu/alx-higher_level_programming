#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});
