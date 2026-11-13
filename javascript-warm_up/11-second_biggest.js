#!/usr/bin/node
let i = 3;
let max = process.argv[2];
while (process.argv[i] !== undefined) {
  let current = parseInt(process.argv[i]);
  if (current > max) {
    max = current;
  }
  i++;
}
console.log(max);
