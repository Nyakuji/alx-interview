#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
