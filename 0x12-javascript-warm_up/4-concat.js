#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('undefined is undefined');
} else if (process.argv[3] === undefined) {
  console.log('c is undefined');
} else {
  console.log('c is cool');
}
