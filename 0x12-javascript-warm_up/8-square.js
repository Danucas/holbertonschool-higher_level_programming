#!/usr/bin/node

const a = Number(process.argv[2]);

if (isNaN(a)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    let line = '';
    for (let i = 0; i < a; i++) {
      line += 'X';
    }
    console.log(line);
  }
}
