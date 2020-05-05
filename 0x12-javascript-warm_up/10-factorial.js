#!/usr/bin/node

const a = Number(process.argv[2]);

function fact (n) {
  if (n >= 1) {
    return n * fact(n - 1);
  } else {
    return 1;
  }
}

if (isNaN(a)) {
  console.log('1');
} else {
  console.log(fact(a));
}
