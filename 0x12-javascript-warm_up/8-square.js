#!/usr/bin/node

const arg = process.argv[2];
if (arg === undefined) {
  console.log('Missing size');
} else if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('x'.repeat(arg));
  }
}
