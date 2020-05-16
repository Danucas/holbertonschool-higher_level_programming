#!/usr/bin/node

const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/';
url += process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const bodyRes = JSON.parse(body);
  console.log(bodyRes.title);
});
