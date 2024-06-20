#!/usr/bin/node

const Arguments = process.argv;
const myStr = 'C is fun';
const num = parseInt(Arguments[2]);

if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(myStr);
  }
}
