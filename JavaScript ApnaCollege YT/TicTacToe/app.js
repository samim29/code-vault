let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#reset-btn");  
let newGameBtn = document.querySelector("#new-btn");
let msgContainer = document.querySelector(".msg-container");
let msg = document.querySelector("#msg");
let turno = true;  // turn of player O
let btnClickCount=0;
const winPatterns = [
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],  
    [6,7,8]
];
const checkDraw = (btnClickCount, isWin) => {
    
        msg.innerText = `Game is Draw`;
        msgContainer.classList.remove("hide");
        disableBoxes();  
    
}
const resetGame = () => {
    turno = true;
    enableBoxes();
    msgContainer.classList.add("hide");
    btnClickCount=0;
    box.style.color="none";
    
};

boxes.forEach((box) => {
    box.addEventListener("click", () => {
        
        if(turno){
            box.innerText = "O";
            box.style.color="red";
            turno = false;
            btnClickCount++;
        } else {
            box.innerText = "X";
            box.style.color="blue";
            turno = true;
            btnClickCount++;
        }
        box.disabled = true;
        
        let isWin = checkWinner();
        if(btnClickCount===9 && !isWin){
           
                checkDraw();
            
        }
        
    });
});

const disableBoxes = () => {  
    for (let box of boxes) {
        box.disabled = true;
    }
};

const enableBoxes = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = "";
    }
};

const showWinner = (winner) => {
    msg.innerText = `Congratulations, Winner is ${winner}`;
    msgContainer.classList.remove("hide");
    disableBoxes();  
};

const checkWinner = () => {
    for (let pattern of winPatterns) {
        let pos1Val = boxes[pattern[0]].innerText;
        let pos2Val = boxes[pattern[1]].innerText;
        let pos3Val = boxes[pattern[2]].innerText;

        if (pos1Val !== "" && pos2Val !== "" && pos3Val !== "") {
            if (pos1Val === pos2Val && pos2Val === pos3Val) {
                boxes[pattern[0]].style.color="green";
                boxes[pattern[1]].style.color="green";
                boxes[pattern[2]].style.color="green";
                showWinner(pos1Val);
                return true;
            }
        }
    }
};


newGameBtn.addEventListener("click", resetGame);
resetBtn.addEventListener("click", resetGame);
