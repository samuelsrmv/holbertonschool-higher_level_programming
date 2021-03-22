#!/usr/bin/node

if (process.argv.length === 4) {
  console.log('c is cool');
} else if (process.argv.length === 3) {
  console.log('c is undefined');
} else {
  console.log('undefined is undefined');
}
