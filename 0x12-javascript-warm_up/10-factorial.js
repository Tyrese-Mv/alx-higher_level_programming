#!/usr/bin/node

const Arguments = process.argv;
const myNum = parseInt(Arguments[2]);

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (Number.isNaN(myNum)) {
  console.log(factorial(1));
} else {
  console.log(factorial(myNum));
}
