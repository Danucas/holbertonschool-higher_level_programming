#!/usr/bin/node

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function findSecondBiggest () {
  let last = a;
  let novo = a;
  let actual;
  for (let i = 2; i < process.argv.length; i++) {
    actual = Number(process.argv[i]);
    if (actual > novo) {
      last = novo;
      novo = actual;
    } else if (actual > last) {
      last = actual;
    }
  }
  if (novo === last) {
    return (0);
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
