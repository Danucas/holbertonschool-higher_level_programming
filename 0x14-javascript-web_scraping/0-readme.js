#!/usr/bin/node

const fs = require('fs');

try {
  const filename = process.argv[2];
  const content = fs.readFileSync(filename, 'utf-8');
  console.log(content);
} catch (err) {
  delete err.stack;
  console.log(err);
}
