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
      let line = '';
      for (let f = 0; f < this.width; f++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
