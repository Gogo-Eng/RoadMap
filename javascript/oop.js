function Person(name, age) {
    this.friend_name = name;
    this.friend_age = age;
}
const person1 = new Person("Richard", 27);
console.log(person1.friend_name);
console.log(person1.friend_age);
