#!/usr/bin/node

const request = require('request');

// Check if the movie ID is provided as a command-line argument
if (process.argv.length < 3) {
  console.log('Usage: node starwars.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// URL to get the movie details
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch data from a given URL
const fetchData = (url, callback) => {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to fetch data:', response.statusCode);
      return;
    }

    callback(JSON.parse(body));
  });
};

// Fetch the movie data
fetchData(movieUrl, (movieData) => {
  const characters = movieData.characters;

  // Fetch and print each character's name
  characters.forEach((characterUrl) => {
    fetchData(characterUrl, (characterData) => {
      console.log(characterData.name);
    });
  });
});
