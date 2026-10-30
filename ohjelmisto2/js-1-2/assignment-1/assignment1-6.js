const asking = confirm("Haluatko laskea jonkin luvun neliöjuuren?");

if (asking === true) {
    const askRoot = parseInt(prompt("Anna numero jonka neliöjuuren haluat laskettavan:"));
    if (askRoot >= 0) {
        const sqrRoot = (x) => {
            console.log("Neliojuuri lasketaan");
            return Math.sqrt(x);
        };
        document.querySelector("#target").innerHTML = "Lukusi neliöjuuri: " + sqrRoot(askRoot);
    } else {
        document.querySelector("#target").innerHTML = "Negatiivisen luvun neliöjuurta ei ole määritelty.";
    }
} else {
    document.querySelector("#target").innerHTML = "Neliöjuurta ei lasketa";
}
