class Person {
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
    talk() {
        console.log(`Hi, ,y name is ${this.name}`);
    }
}



class Student extends Person{
    constructor(name,age,marks){
        super(name,age);
        this.marks = marks;
    }
    greet(){
        return "hello";
    }
}
let p1 = new Person("samim",22);
console.log(p1);

let s1 = new Student("sadik",22,100);
