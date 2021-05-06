#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const arg_ = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + arg_;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const json_ = JSON.parse(body);
  for (const property of json_.characters) {
    request(property, function (er, response, body) {
      if (er) {
        return console.log(er);
      }
      const name_ = JSON.parse(body);
      console.log(name_.name);
    }
    );
  }
});
