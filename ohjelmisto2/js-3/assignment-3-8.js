const lista = ["Johnny", "DeeDee", "Joey", "Marky"];

const concat = (list) => {
    const summing = list[0] + list[1] + list[2] + list[3];
    return summing;
}

document.querySelector("#target").innerHTML = concat(lista);

// Karvahattumalli tehtävänannosta :D