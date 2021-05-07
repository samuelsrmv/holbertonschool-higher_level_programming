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
  const promesas = [];
  for (const property of json_.characters) {
    const promise = new Promise(function (resolve, reject) {
      request(property, function (er, response, body) {
        if (er) {
          return reject(er);
        }
        const name_ = JSON.parse(body).name;
        resolve(name_);
      });
    });
    promesas.push(promise);
  }
  Promise.all(promesas).then(function (resultado) {
    for (const x of resultado) {
      console.log(x);
    }
  }).catch(function (res) {
    console.log(res);
  });
});
