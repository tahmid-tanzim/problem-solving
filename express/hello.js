class Student {
    cgpa;
    constructor(name) {
        this.name = name;
    }

    setCGPA(val) {
        this.cgpa = val
    }

    getName() {
        return this.name
    }
}

const s1 = new Student("lupin");
console.log(s1.name);