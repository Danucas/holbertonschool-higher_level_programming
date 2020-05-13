#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log('code:', res.statusCode);
  } else {
    let count = 0;
    const bodyRes = JSON.parse(body).results;
    const us = '/18/';
    for (const resp of bodyRes) {
      for (const chara of resp.characters) {
        if (chara.endsWith(us)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
