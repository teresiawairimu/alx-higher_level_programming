#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;
request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  console.log(`${data.title}`);
});
