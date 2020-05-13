#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log('code:', res.statusCode);
  } else {
    let count = 0;
    const bodyRes = JSON.parse(body).results;
    const userString = 'https://swapi-api.hbtn.io/api/people/18/';
    for (const resp of bodyRes) {
      if (resp.characters.indexOf(userString) > -1) {
        count++;
      }
    }
    console.log(count);
  }
});
