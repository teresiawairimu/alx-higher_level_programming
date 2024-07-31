#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) reject(err);
        else resolve(JSON.parse(body).name);
      });
    });
  };
  const printCharacters = async () => {
    for (const characterUrl of characters) {
      const name = await fetchCharacter(characterUrl);
      console.log(name);
    }
  };
  printCharacters();
});
