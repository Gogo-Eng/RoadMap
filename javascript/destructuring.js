const Student = {
    studentname: "Gogo",
    class: "SS3",
    age: 16,
    sex: "Male"
}

// destructuring
const { studentname: name, sex, State = "Lagos" } = Student;
// renaming, direct assignment and default value
console.log(name);
console.log(Student.age);
console.log(Student.class);
console.log(sex);
