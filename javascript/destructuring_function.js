const Student = {
    studentname: "Gogo",
    class: "SS3",
    age: 16,
    sex: "Male"
}

function astatus({studentname: name, age }) {
    console.log( name + "@" + age);
}

astatus(Student);