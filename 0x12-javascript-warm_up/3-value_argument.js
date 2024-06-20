#!/usr/bin/node

const Arguments = process.argv;

if (!(Arguments[2])) {
  console.log('No argument');
} else {
  console.log(Arguments[2]);
}
