#!/usr/bin/node
let i = 3;
if (process.argv.length <= 3) {
  console.log(0);
  process.exit(0);
}
let max = parseInt(process.argv[2], 10);
let secondMax = -Infinity;

while (process.argv[i] !== undefined) {
  const current = parseInt(process.argv[i], 10);
  if (current > max) {
    secondMax = max;
    max = current;
  } else if (current > secondMax) {
    secondMax = current;
  }
  i++;
}
console.log(secondMax);
