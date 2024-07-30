#!/usr/bin/node
//script that writes a string to a file.

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
	console.error('Please provide the API URL as the first argument.');
	process.exit(1);
}

request(apiUrl, (error, response, body) => {
	try {
		const todos = JSON.parse(body);
		const completedTasks = {};

		todos.forEach(todo => {
			if (todo.completed) {
				if (!completedTasks[todo.userId]) {
					completedTasks[todo.userId] = 0;
				}
				completedTasks[todo.userId]++;
			}
		});
		console.log(completedTasks);
	} catch (parseError) {
		console.error('Error parsing JSON:', parseError);
	}
});

