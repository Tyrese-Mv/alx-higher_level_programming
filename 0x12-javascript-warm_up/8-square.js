#!/usr/bin/node

const Arguments = process.argv;
const size = parseInt(Arguments[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let eachRow = '';
    for (let j = 0; j < size; j++) {
      eachRow += 'X';
    }
    console.log(eachRow);
  }
}
