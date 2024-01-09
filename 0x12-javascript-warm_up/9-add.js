#!/usr/bin/node
function add (a, b) {
  const vr = a + b;
  console.log(vr);
}

add(Number(process.argv[2]), Number(process.argv[3]));
