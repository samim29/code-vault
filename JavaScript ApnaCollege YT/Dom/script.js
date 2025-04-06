// let heading = document.querySelector("h2");
// heading.innerText = heading.innerText + " from Apna College Students";

// let divs = document.querySelectorAll(".mydiv");
// console.dir(divs);
// let i =0;
// for(let div of divs){
//     div.innerText = `new unique value ${i}`
//     i++;
// }

// let div = document.querySelector("div");
// console.log(div.getAttribute("id"));
// div.setAttribute("id","divId");
// console.log(div.getAttribute("id"));


//Q. Create a new button element. give it a text "click me",background color of red
// &text color of white. insert the button as the first element inside the body tag.

let btn = document.createElement("button");
btn.innerText = "click me";
btn.style.backgroundColor = "red";
btn.style.color="white";

let body = document.querySelector("body");
body.prepend(btn);

// question 2 dom part 2 apna cllg you tube
let p = document.querySelector("p");
p.classList.add("newClass");
// p.setAttribute("class","newPara");

// let classes = p.classList
// console.log(classes);
// classes.add("new para 2");
// console.log(classes);