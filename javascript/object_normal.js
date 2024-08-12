const person = {
    firstName: "Nick",
    lastName: "Anderson",
    age: 35,
    sex: "M"
  }

const first = person.firstName;
const age = person.age;
const city = person.city || "Paris";  //default value

console.log(age);
console.log(city);
console.log(first);
