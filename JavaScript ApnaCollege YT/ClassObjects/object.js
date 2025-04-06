// const student = {
//     name : "Sk Samim Ali",
//     marks : 94.4,
//     printMarks : function (){
//         console.log("marks = ",this.marks);
//     },
// };


// const student = {
//     name : "Sk Samim Ali",
//     marks : 94.4,
//     printMarks(){
//         console.log("marks = ",this.marks);
//     },
// };


//constructor

// class ToyotaCar{
//     constructor(){
//         console.log("creating new object");
//     }
//     start(){
//         console.log("start");
//     }
//     stop(){
//         console.log("stop");
//     }
//     setBrand(brand){
//         this.brand=brand;
//     }
// }

// let fortuner = new ToyotaCar();//constructor invoked
// let lexus = new ToyotaCar();//constructor invoked


class User{
    constructor(name ,email){
        this.name = name;
        this.email = email;
    }
    viewData(){
        console.log("Viewing Data","Name = ",this.name, "email = ",this.email);
    }
}

let user1 = new User("samim","samimalisk000@gmail.com");
let user2 = new User("Upasana","upasanasarkar404@gmail.com");

user1.viewData();
user2.viewData();