#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBaseTen (num) {
    return parseInt(num).toString(base);
  };
};
