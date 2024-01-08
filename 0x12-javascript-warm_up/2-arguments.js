#!/usr/bin/node

const Arguments = process.argv;
const numArguments = Arguments.length - 2;

if (numArguments === 1) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
