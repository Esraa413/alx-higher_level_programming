#!/usr/bin/node
let vr = 0;
exports.logMe = function (item) {
  console.log(vr + ': ' + item);
  vr++;
};
