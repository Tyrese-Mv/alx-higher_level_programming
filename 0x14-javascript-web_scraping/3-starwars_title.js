#!/usr/bin/node
//script that writes a string to a file.

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
	try {
		const data = JSON.parse(body);
		console.log(data.title);
	} catch (parseError) {
		console.error('Error parsing JSON:', parseError);
	}
});

