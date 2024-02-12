#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// use the url to fetch the film
request(filmUrl, (err, body) => {
    if (err) console.error(err);
    console.log(data);
});
// access all characters through => .characters which is a list
// loop thro array, printing characters