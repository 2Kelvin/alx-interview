#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

function recursiveXterNameFetch (allXtersUrl) {
  if (allXtersUrl.length === 0) return;

  // chop off, return and use each character url from the start one by one
  const xterUrl = allXtersUrl.shift();
  request(xterUrl, (err, response, body) => {
    if (err) console.error(err);
    const xterObject = JSON.parse(body);
    console.log(xterObject.name);

    // after displaying first character name, move to the next character
    // remember shift removes the first element, returns it and ...
    // ... shifts the array items i.e the 2nd character is now the 1st
    // ...the 3rd is the 2nd and so on
    recursiveXterNameFetch(allXtersUrl);
  });
}

request(filmUrl, (error, resp, bdy) => {
  if (error) console.error(error);
  const data = JSON.parse(bdy);
  const movieXtersArray = data.characters;

  // make a copy of the api film characters as it is
  recursiveXterNameFetch(movieXtersArray.slice());
});
