#!/usr/bin/node

const Arguments = process.argv.slice(2);
const myArr = Arguments.map(Arguments => parseInt(Arguments));
const sorted = myArr.sort(function (a, b) {
  return b - a;
});

if (sorted.length < 2) {
  console.log('0');
} else {
  console.log(sorted[1]);
}
