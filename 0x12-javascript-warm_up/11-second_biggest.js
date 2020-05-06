#!/usr/bin/node

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function findSecondBiggest () {
  let prettyLast = 0;
  let last = 0;
  let novo = a;
  let actual;
  for (let i = 2; i < process.argv.length; i++) {
    actual = Number(process.argv[i]);
    if (actual > novo) {
      if (prettyLast !== last) {
        prettyLast = last;
      }
      last = novo;
      novo = actual;
    } else if (actual > last && actual !== novo) {
      if (prettyLast !== last) {
        prettyLast = last;
      }
      last = actual;
    }
  }
  if (novo === last) {
    return (prettyLast);
  } else {
    return (last);
  }
}

if (isNaN(a)) {
  console.log('0');
} else if (isNaN(b)) {
  console.log('0');
} else {
  console.log(findSecondBiggest());
}
