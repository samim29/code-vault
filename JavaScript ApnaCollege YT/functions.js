//Q. create a function using the fuunction keyword that takes a string as an argument & returns the number of vowels in the string

// function countVowel(str){
//     let count = 0;
//     for(const char of str.toLowerCase()){
//         if (char =="a" || char == "e" || char == "i" || char == "o" || char == "u" ){
//             count++;
//         }
//     }
//     return count;
// }

// console.log(countVowel("Hi! I am learning Java Script"));

// create a arrow function to perform the same task

// const countVowels = (str) => {
//     let count = 0;
//     for(const char of str.toLowerCase()){
//         if (char =="a" || char == "e" || char == "i" || char == "o" || char == "u" ){
//             count++;
//         }
//     }
//     return count;
// }
// console.log(countVowels("Hi! I am learning Java Script"));


//forEach() Loop

// let arr = [1,2,3,4,5,6,7];
// arr.forEach(element => {
//     console.log(element**2);
// });

//Question: Given array of marks of students. Filter out the marks of students that scored 90+.
 
// let marksArr = [87, 90, 95,93,10,87,96];

// let filterArr = marksArr.filter(item=> item > 90)
// console.log(filterArr)

//Q. take a number n as input from user. Create an array of numbers from 1 to n. then use reduce to calculate sum and multiplication
