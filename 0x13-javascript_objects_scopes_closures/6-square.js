#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      let v = '';
      for (let t = 0; t < this.width; t++) {
        v += c;
      }
      console.log(v);
    }
  }
}
module.exports = Square;
