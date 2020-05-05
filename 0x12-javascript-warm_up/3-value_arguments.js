#!/usr/bin/node

let count = 0;
process.argv.forEach(arg => {
  if (count === 2) {
    console.log(arg);
  }
  count++;
});
if (count === 2) {
  console.log('No argument');
}
