#!/usr/bin/node

const axios = require('axios');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./get_starwars_characters.js <movie_id>');
  process.exit(1);
}

// Function to fetch and display the characters of the specified movie
async function getStarWarsCharacters (movieId) {
  try {
    // Fetch movie data from the Star Wars API
    const filmResponse = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const movieData = filmResponse.data;

    // Loop through the character URLs and fetch each character's name
    for (const characterUrl of movieData.characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

// Call the function to fetch and display the characters
getStarWarsCharacters(movieId);
