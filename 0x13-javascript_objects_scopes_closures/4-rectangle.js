#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

print () {
    for (let j = 0; j < this.height; j++) {
      let v = '';
      for (let t = 0; t < this.width; t++) {
        v += 'X';
      }
      console.log(v);
    }
  }

rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
