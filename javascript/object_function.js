const Student = {
    studentname: "Gogo",
    class: "SS3",
    age: 16,
    sex: "Male"
}

function astatus(Student) {
    const name = Student.studentname;
    const age = Student.age;
    const classs = Student.class;
    const sex = Student.sex;
    
    console.log(sex);
    console.log(name);
    console.log(age);
    console.log(classs);
}

astatus(Student);