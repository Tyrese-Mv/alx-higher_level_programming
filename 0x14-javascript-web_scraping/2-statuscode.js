#!/usr/bin/node
//script that writes a string to a file.
const request = require('request');

const url = process.argv[2];
request.get(url, (error, response, body) => {
	console.log(`code: ${response.statusCode}`);
});

