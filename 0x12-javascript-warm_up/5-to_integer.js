#!/usr/bin/node

const Arguments = process.argv;
let num = parseInt(Arguments[2])
if (Number.isNaN(num)){
    console.log('Not a number');
}else{
    console.log('My number: ' + num);
}