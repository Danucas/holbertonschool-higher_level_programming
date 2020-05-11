#!/usr/bin/node

exports.converter = function (base) {
  this.base = base;

  function convert (number) {
    return (parseInt(number, 10).toString(this.base));
  }
  return (convert);
};
