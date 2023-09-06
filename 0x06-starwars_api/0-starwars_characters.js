#!/usr/bin/node
// get star wars films and check number of films that
// print characters to screen 
const request = require('request');
const filmId = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + filmId, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  const res = JSON.parse(response.body);
  const characters = res.characters;
  let charUrl;
  for (let j = 0; j < characters.length; j++) {
    charUrl = characters[j];
    request(charUrl, function (error, response, body) {
      if (error) {
        console.error('error', error);
      }
      const data = JSON.parse(response.body);
      console.log(data.name);
    });
  }
});
