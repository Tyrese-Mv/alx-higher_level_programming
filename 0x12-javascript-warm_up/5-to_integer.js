#!/usr/bin/node

const Arguments = process.argv;
const num = parseInt(Arguments[2]);
if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
