#!/usr/bin/node
const num1 = parseInt(process.argv[2]);

if (isNaN(num1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num1);
}  
