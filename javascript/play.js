// play.js
const firstNumber = process.argv[2];
const secondNumber = process.argv[3];

if (!firstNumber || !secondNumber) {
  console.log('Usage: node play.js <first_number> <second_number>');
  process.exit(1);
}

console.log(`The sum of ${firstNumber} and ${secondNumber} is: ${Number(firstNumber) + Number(secondNumber)}`);
