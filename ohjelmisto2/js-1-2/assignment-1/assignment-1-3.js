const numberone = parseInt(prompt("Anna ensimmäinen numero:"))
const numbertwo = parseInt(prompt("Anna toinen numero:"))
const numberthree = parseInt(prompt("Anna kolmas numero:"))

// function numberActions(x, y, z) {
//     const summa = x + y + z
//     const tulo = x * y * z
//     const karvo = (x + y + z) / 3
//     return;
// }

const numbersum = (x, y, z) => {
    console.log("Numeroiden summaa kutsuttu");
    return x + y + z;
};
const numberproduct = (x, y, z) => {
    console.log("Numeroiden tulo kutsuttu");
    return x * y * z;
}
const numberaverage = (x, y, z) => {
    console.log("Numeroiden keskiarvo kutsuttu");
    return (x + y + z) / 3;
}
document.querySelector("#target").innerHTML = "Numeroidesi summa: " + numbersum(numberone, numbertwo, numberthree) + "<br />Numeroidesi tulo: " + numberproduct(numberone, numbertwo, numberthree) + "<br />Numeroidesi keskiarvo: " + numberaverage(numberone, numbertwo, numberthree)
