#!/usr/bin/node
//script that writes a string to a file.

const request = require('request');

const apiUrl = process.argv[2];

const wedgeAntillesId = '18';

request(apiUrl, (error, response, body) => {
	try {
		const data = JSON.parse(body);
		let count = 0;
		data.results.forEach(film => {
			if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
				count++;
			}
		});
		console.log(count);
	} catch (parseError) {
		console.error('Error parsing JSON:', parseError);
	}
});

