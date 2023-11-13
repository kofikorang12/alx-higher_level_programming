#!/usr/bin/node
let list_arg = process.argv;
list_arg.shift();
list_arg.shift();
list_arg.forEach(function (element, index) {
  list_arg[index] = parseInt(element);
});
list_arg.splice(list_arg.indexOf(Math.max(...list_arg)), 1);
if (list_arg.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...list_arg));
}
