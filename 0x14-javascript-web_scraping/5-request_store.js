#!/usr/bin/node
//script that writes a string to a file.
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
	try {
		fs.writeFile(filePath, body, 'utf-8', (err) => {
		if (err) {
			console.error(err);
		}
	});
	} catch (parseError) {
		console.error('Error parsing JSON:', parseError);
	}
});

