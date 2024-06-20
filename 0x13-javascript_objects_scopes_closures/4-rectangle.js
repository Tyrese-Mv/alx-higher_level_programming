#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp1 = this.height;
    const temp2 = this.width;
    this.height = temp2;
    this.width = temp1;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
