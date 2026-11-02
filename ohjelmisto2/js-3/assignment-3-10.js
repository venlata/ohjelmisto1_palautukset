const voterAmount = parseInt(prompt("Anna äänestäjien lukumäärä:"));

const voteForThese = [
    {
        name: "ellie",
        votes: 0,
    },
    {
        name: "frank",
        votes: 0,
    },
    {
        name: "pamela",
        votes: 0,
    },
];

for (let voter = 1; voter <= voterAmount; voter++){
    const voting = prompt("Ketä äänestät? \nellie \nfrank \npamela")
    switch (voting){
        case "ellie":
            console.log("Äänestit ellie");
            voteForThese[0].votes += 1;
            break;
        case "frank":
            console.log("Äänestit frank");
            voteForThese[1].votes += 1;
            break;
        case "pamela":
            console.log("Äänestit pamela");
            voteForThese[2].votes += 1;
            break;
        case "":
            console.log("Ääni haaskattu, ei nimeä");
            break;
        default:
            console.log("Väärä nimi, ääni haaskattu");
    }
};

voteForThese.sort((a, b) => b.votes - a.votes);

let winner = voteForThese[0]

console.log("Voittaja on " + winner.name+ " " + winner.votes + " pisteellä.");
console.log("Tulokset:");

voteForThese.forEach(votees => {
    console.log(votees.name + ": " + votees.votes + " pistettä");
}
);

document.querySelector("#target").innerHTML = "Voittaja: " + voteForThese[0].name