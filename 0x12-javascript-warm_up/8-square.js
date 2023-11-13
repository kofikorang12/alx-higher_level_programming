#!/usr/bin/node
let size_square = parseInt(process.argv[2]);
if (isNaN(size_square) === true) {
  console.log("Missing size");
} else {
  for (let i = sizesize_square; i > 0; i--) {
    console.log("X".repeat(sizesize_square));
  }
}
