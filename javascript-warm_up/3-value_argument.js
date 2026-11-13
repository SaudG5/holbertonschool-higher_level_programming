#!/usr/bin/node
const count = process.argv[2];

if (count === undefined) {
  console.log('No argument');
} else {
  console.log(count);
}
