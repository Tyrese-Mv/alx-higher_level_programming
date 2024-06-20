#!/usr/bin/node

exports.esrever = function (list) {
  const myArr = [];

  for (let i = list.length - 1; i > -1; i--) {
    myArr.push(list[i]);
  }
  return myArr;
};
