#!/usr/bin/node
function add (a, b) {
	const m = a + b;
	console.log(m);
}

add(Number(process.argv[2]), Number(process.argv[3]));
