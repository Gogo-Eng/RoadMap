const character = "#";
const count = 8;
const rows = [];
done = 0;
continueloop = true;

function padRow(rowNumber, rowCount) {
  return ".".repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + ".".repeat(rowCount - rowNumber);
}

while (continueloop) {
   done++;
   rows.push(padRow(done, count));

   if (done !== count) {
        continueloop = true;
   }
   else {
    continueloop =  false;
   }
  }

  let result = "";
  for (const row of rows) {
    result = result + row  + "\n"; /** row + result will reverse the pyramid*/
  }
  console.log(result);
  console.log(rows);