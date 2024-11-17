#!/usr/bin/node

const https = require('https');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./get_starwars_characters.js <movie_id>');
  process.exit(1);
}

// Helper function to make HTTPS requests
function fetch (url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (error) {
          reject(new Error('Failed to parse JSON'));
        }
      });
    }).on('error', (error) => {
      reject(error);
    });
  });
}

// Main function to fetch and display the characters of the specified movie
async function getStarWarsCharacters (movieId) {
  try {
    // Fetch movie data from the Star Wars API
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    const movieData = await fetch(filmUrl);

    // Loop through the character URLs and fetch each character's name
    for (const characterUrl of movieData.characters) {
      const characterData = await fetch(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

// Call the function to fetch and display the characters
getStarWarsCharacters(movieId);
