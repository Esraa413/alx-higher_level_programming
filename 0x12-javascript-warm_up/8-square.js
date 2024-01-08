#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const j = Number(process.argv[2]);
  let x = 0;
  while (x < j) {
    console.log('X'.repeat(x));
    x++;
  }
}
