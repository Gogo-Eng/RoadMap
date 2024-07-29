const character = "#";
const count = 8;
const rows = [];

function padRow(rowNumber, rowCount) {
  return ".".repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + ".".repeat(rowCount - rowNumber);
}

while (rows.length < count) {
   rows.push(padRow(rows.length +1, count));

  }

  let result = "";
  for (const row of rows) {
    result = result + row  + "\n"; /** row + result will reverse the pyramid*/
  }
  console.log(result);
  console.log(rows);