#!/usr/bin/node

const _Square = require('./5-square');
module.exports = class Square extends _Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let h = 0; h < this.width; h++) {
      console.log(c.repeat(this.height));
    }
  }
};
