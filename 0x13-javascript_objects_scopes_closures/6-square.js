#!/usr/bin/node
const Squ = require('./5-square');

module.exports = class Square extends Squ {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let f = 0; f < this.width; f++) {
        line += c;
      }
      console.log(line);
    }
  }
};
