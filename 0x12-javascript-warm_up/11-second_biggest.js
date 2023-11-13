#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(Number);

if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
