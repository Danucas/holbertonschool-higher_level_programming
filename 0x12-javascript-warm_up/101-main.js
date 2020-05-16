#!/usr/bin/node
const callMeMoby = require('./102-add_me_maybe').addMeMaybe;
callMeMoby(3, function (nb) {
  console.log('Value is: ', nb)
});