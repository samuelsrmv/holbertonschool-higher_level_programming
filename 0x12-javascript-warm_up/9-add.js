#!/usr/bin/node

const firstnumebr = process.argv[2];
const secondnumer = process.argv[3];

if (isNaN(firstnumebr) || isNaN(secondnumer)) {
  console.log('NaN');
} else {
  console.log(add(parseInt(firstnumebr), parseInt(secondnumer)));
}

function add (a, b) {
  return a + b;
}
