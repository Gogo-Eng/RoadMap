const person_1 = {
    parent: ["Gogo", "Bettty"],
    firstname:"Progress",
    lastname: "Gogo",   //properties
    age: 25,
    is_employed: false,
    bio: function(){console.log(`my dad's name is ${this.parent[0]}, and my mum's name is ${this.parent[1]}`)},
    sayhello: function(){console.log("Hi!, i'm Progress")},
    eat: () => console.log("i'm eating fufu"),
    lot: function(family_name){console.log(person_1[family_name])},
};

function list(familyname) {console.log(person_1[familyname])};
person_1.lot("parent");
list("parent");
console.log(person_1.firstname);
console.log(person_1.lastname);
console.log(person_1.age);
console.log(person_1.is_employed);
person_1.sayhello();
person_1.eat();
person_1.bio();
person_1["parent"]["last"] = "Cratchit";
person_1["parent"]["2"] = "God";
person_1.eyes = "hazel";
person_1.farewell = function(){ console.log("Bye everybody!");};

console.log(person_1.eyes);
console.log(person_1["parent"]["last"] = "Cratchit");
console.log(person_1.parent)
person_1.farewell();

const person_2 = {
    firstname: "Yemmy",
    lastname: "Eteng",   //properties
    age: 25,
    is_employed: true,
    sayhello: function(){console.log("Hi!, i'm Yemmy")},
    eat: () => console.log("i'm eating rice"),  //arrow function
};

console.log(person_2.firstname);
console.log(person_2.lastname);
console.log(person_2.age);
console.log(person_2.is_employed);
person_2.sayhello();
person_2.eat();

