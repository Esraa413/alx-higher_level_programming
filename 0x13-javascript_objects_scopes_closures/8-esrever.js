#!/usr/bin/node
exports.esrever = function (list) {
  let vr = list.length - 1;
  let j = 0;
  while ((vr - j) > 0) {
    const aux = list[vr];
    list[vr] = list[j];
    list[j] = aux;
    j++;
    vr--;
  }
  return list;
};
