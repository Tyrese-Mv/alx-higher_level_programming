#!/usr/bin/node

const Arguments = process.argv;
const num1 = parseInt(Arguments[2]);
const num2 = parseInt(Arguments[3]);

function add (a, b) {
  return a + b;
}

console.log(add(num1, num2));
