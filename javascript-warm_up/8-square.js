#!/usr/bin/node
const size = process.argv[2];
const arg1 = parseInt(size);

if (isNaN(arg1)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < arg1; i++) {
        for (let j = 0; j < arg1; j++) {
            console.log('X');
        }
    }
}
