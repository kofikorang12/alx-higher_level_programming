#!/usr/bin/node
let my_Integer = parseInt(process.argv[2], 10);
if (isNaN(my_Integer) === true) {
  console.log("Not a number");
} else {
  console.log("My number: " + my_Integer);
}
