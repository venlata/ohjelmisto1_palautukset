const diceAmount = parseInt(prompt("Montako kertaa noppia heitetään:"));
//const diceRoll = Math.random(0, 7)

// const diceThrow = () => {
//     console.log("Nopanheitto suoritettu");
//     const minCeiled = Math.ceil(0);
//     const maxFloored = Math.floor(7);
//     return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
// }


// for (let i = 0; i <= diceAmount; i++) {
//     diceThrow();
//     console.log(diceThrow());
// }

let sumOfDice = 0;

for (let i = 0; i < diceAmount; i++) {
    const eyeAmountOfThrow = Math.floor(Math.random() * 6) + 1;
    sumOfDice += eyeAmountOfThrow;
    console.log(eyeAmountOfThrow);
};


document.querySelector("#target").innerHTML = "Nopanheittojen numeroiden summa: " + sumOfDice;
