const button = document.getElementById("button-54");
let min = document.getElementById("srange");
let max = document.getElementById("erange");
let p = document.getElementById("p");
let s = document.getElementById("s");


let guesses = 0;
let cguesses = 0;

let answer=null;

button.onclick = function(){
    min = Number(min.value);
    max = Number(max.value);
    
    answer = Math.floor(Math.random() * (max - min + 1)) + min;
    
    let guess = Number(window.prompt(`guess a number between ${min} and ${max}`));

    if(guess === answer){
        window.alert("you guessed it");
        guesses++;
    }
    else{
        window.alert("wrong guess");
        cguesses++;
    }

    p.textContent = `${guesses}`;
    s.textContent = `${cguesses}`;
}
