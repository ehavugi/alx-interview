#!/usr/bin/node
// get star wars films and check number of films that
// edge Antilles, character ID 18  is in and return
// the numbers to console
const request = require('request');
const filmId = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + filmId, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  const res = JSON.parse(response.body);
  const characters = res.characters;
  let charUrl;
  const names = {};
  let out = 0;
  for (let j = 0; j < characters.length; j++) {
    charUrl = characters[j];
    request(charUrl, function (error, response, body) {
      if (error) {
        console.error('error', error);
      }
      const data = JSON.parse(response.body);
      names[j] = data.name;
      out += 1;
      if (out === characters.length) {
        for (let i = 0; i < characters.length; i++) {
          console.log(names[i]);
        }
      }
    });
  }
});
