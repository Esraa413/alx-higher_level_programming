#!/usr/bin/node
function factorial (vr) {
  if (vr < 0) {
    return (-1);
  }
  if (vr === 0 || isNaN(vr)) {
    return (1);
  }
  return (vr * factorial(vr - 1));
}

console.log(factorial(Number(process.argv[2])));
