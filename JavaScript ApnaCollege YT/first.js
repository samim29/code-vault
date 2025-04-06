// const product={
//     name:"Parker Jotter Standard Ball Pen",
//     rating:4,
//     offer:5,
//     price:270

// };
// console.log(product)

// const shradhakhapra = {
//     userName: "@shradhakhapra",
//     isFollow: false,
//     followers:123,
//     following:123
// }

// let str = "Sk Samim Ali";
// console.log(str.slice(-5));

// let str = prompt("Enter your name: ");
// console.log(`Your user name is @${str.toLocaleLowerCase()+str.length}`);

//Question to find average
// let marksArray = [85,97,44,37,76,60]
// let sum = 0;
// for(let marks of marksArray){
//     sum += marks;
// }
// console.log(`Average marks is ${sum/marksArray.length}`);

//Find final price after applying 10% offer

// let prices = [250,645,300,900,50];
// for (let i = 0 ; i<prices.length ; i++){
//     prices[i] -= prices[i] * 0.1;    
// }
// console.log(prices);


 //question

 let companies = ["Bloomberg", "Microsoft", "Uber", "Google", "IBM", "Netflix"];
 console.log(`removing the first element ${companies.shift()}`);
 console.log("Current array is",companies,"\n");
companies.splice(1,1,"Ola");
console.log("removing Uber and adding Ola in its place",companies,"\n");
companies.push("Amazon");
console.log("Adding Amazon at the end",companies);


