#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
