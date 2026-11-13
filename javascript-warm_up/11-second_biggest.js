#!/usr/bin/node
let i = 3;
let max = process.argv[2];
let secondMax = 0;
while (process.argv[i] !== undefined) {
  let current = parseInt(process.argv[i]);
  if (current > max) {
    secondMax = max;
    max = current;
  } else if (current > secondMax) {
    secondMax = current;
  }
  i++;
}
console.log(secondMax);
