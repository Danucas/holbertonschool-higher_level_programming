#!/usr/bin/node

const a = Number(process.argv[2]);

if (isNaN(a)) {
  console.log('Not a number');
} else {
  console.log(a);
}
