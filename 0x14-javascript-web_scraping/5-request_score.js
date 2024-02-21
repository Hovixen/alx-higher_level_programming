#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const [,, arg] = process.argv;

request(arg, (error, response, body) => {
	if (error) {
		console.error(error);
		return;
	}
