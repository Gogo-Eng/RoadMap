function Person(name, age) {
    this.name = name;
    this.age = age;
}

const person1 = new Person("Richard", 27);
// adding as method to the prototype
Person.prototype.greeting = function(status, time) {
    console.log(`Hello ${status}, good ${time}`);
};

person1.greeting("Sir", "afternoon");