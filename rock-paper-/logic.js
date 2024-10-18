let userscore=0;
let compscore=0;
const choices=document.querySelectorAll(".choice");
const msg=document.querySelector("#msg");
const userpara=document.querySelector("#your-score");
const comppara=document.querySelector("#comp-score");
const drawGame = () =>{
    console.log("Game draw");
    msg.innerText="Game Draw.Play Again"
    msg.style.backgroundColor="blue";
}
const gencompChoice = ()=>{
    const options = ["rock","paper","scissors"];
   const randid= Math.floor(Math.random()*3);
   return options[randid];

}
const playgame =(userChoice) =>{
    console.log("userchoice=",userChoice);
    const compChoice=gencompChoice();
    console.log("compchoice=",compChoice);
    if(userChoice==compChoice){
        drawGame();
    }
    else{
        let userWin=true;
        if(userChoice === "rock"){
           userWin= compChoice === "paper" ? false : true;
        }
        else if(userChoice === "paper"){
            userWin=compChoice === "scissors" ? false : true;
        }
        else{
            userWin=compChoice === "rock" ? false : true;
        }
        showWinner(userWin);
    }
}
choices.forEach((choice) =>{
    choice.addEventListener("click",() =>{
      const userChoice=choice.getAttribute("id");
        playgame(userChoice);
    });
});
const showWinner = (userWin) =>{
    if(userWin){
        userscore++;
        userpara.innerText=userscore;
        console.log("You Win!Congratulations :-)");
        msg.innerText="You Win! :-) Congratulations";
        msg.style.backgroundColor="green";
    }
    else{
        compscore++;
        comppara.innerText=compscore;
        console.log("Sorry! :-( Better luck next Time");
        msg.innerText="Sorry :-( Better luck next Time";
        msg.style.backgroundColor="red";
    }
}