#!/usr/bin/node

const Arguments = process.argv;
const argLength = Arguments.length;

const myArr = [];
if (argLength === 2) {
  console.log('0');
} else if (argLength === 3) {
  console.log('1');
} else {
  for (let i = 2; i < argLength; i++) {
    myArr.push(parseInt(Arguments[i]));
  }
  myArr.sort(function (a, b) {
    return b - a;
  });
  console.log(myArr[1]);
}
