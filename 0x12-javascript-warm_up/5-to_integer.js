#!/usr/bin/node
const args = process.argv.slice(2);
const firstArgument = args[0];
const number = parseInt(firstArgument, 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
