const character = "#";
const count = 8;
const rows = [];

function padRow(rowNumber, rowCount) {
  return ".".repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + ".".repeat(rowCount - rowNumber);
}

for (let i = 0; i < count; i = i + 1) {     // for (let i = count; i > 0; i = i - 1) {
  rows.push(padRow((i + 1), count));        //    rows.push(padRow(i, count));
}                                           // }  This is reverse
  
  let result = "";
  for (const row of rows) {
    result = result + row  + "\n"; /** row + result will reverse the pyramid*/
  }
  console.log(result);
  console.log(rows);