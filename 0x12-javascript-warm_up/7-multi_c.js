#!/usr/bin/node
const occure = Number(process.argv[2]);
if (occure) {
  for (let index = 0; index < occure; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurre');
}
