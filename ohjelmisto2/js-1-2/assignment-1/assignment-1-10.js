const diceAmount = parseInt(prompt("Anna noppien lukumäärä:"))
const eyeAmount = parseInt(prompt("Anna noppien silmälukujen määrä:"))

// const dicethrow = (x) => {
//     console.log("Nopanheitto suoritettu");
//     return Math.random(0, x);
// }
const odds = (x, y) => {
    console.log("Lasketaan todennäköisyyttä");
    const diceRoll = Math.random(0, y);
    const oddsnumbers = [];
    // const howManyDice = x
    const allDiceRoll = x * diceRoll;
    for (let i = 0; i < 10000; i++) {
        allDiceRoll
        oddsnumbers.push(i)
    };
    const ynumbers = [];
    for (const number of oddsnumbers){
        if (number === y)

    }
    
}
