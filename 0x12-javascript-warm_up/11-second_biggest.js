#!/usr/bin/node

const Arguments = process.argv.slice(2);
const myArr = Arguments.map(Arguments => parseInt(Arguments));
const numCheck = myArr.filter(myArr => !isNaN(myArr));
const sorted = numCheck.sort((a, b) => b - a);

if (sorted.length < 2) {
  console.log('0');
} else {
  console.log(sorted[1]);
}
