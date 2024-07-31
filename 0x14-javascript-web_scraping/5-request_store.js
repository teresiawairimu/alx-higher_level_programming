#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to the file:', err);
      process.exit(1);
    }
    console.log('successful');
  });
});
