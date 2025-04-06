// let num=prompt("Enter a number: ");
// console.log(num%2==0?"Even":"Odd");

// let str = "ApnaCollege";
// for (let i of str){
//     console.log("i=", i);
// }

let gameNumber=25;
let userNum=prompt("Guess the number");


while(userNum!=gameNumber){
    alert("try again!");
    userNum=prompt("Guess the number");    
}
alert("You Won!");
