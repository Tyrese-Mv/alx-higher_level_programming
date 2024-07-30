#!/usr/bin/node
//script that writes a string to a file.
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
	console.error('Please provide a file path and a string to write as arguments.');
	process.exit(1);
}
fs.writeFile(filePath, content, 'utf-8', (err) => {
	if (err) {
		console.error(err);
	}
});

