#!/usr/bin/node
//script that reads and prints the content of a file.

const fs = require('fs');
const filePath = process.argv[2];
if (!filePath) {
	console.error('Please provide a file path as the first argument.');
	process.exit(1);
}
fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
		return;
	}
	console.log(data);
});

