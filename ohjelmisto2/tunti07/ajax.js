

setTimeout(function () {
  console.log("Tämä viesti tulostetaan kerran 2,5 sekunnin kuluttua");
}, 2500);

setInterval(function () {
  console.log("Tämä viesti tulostetaan 5 sekunnin välein");
}, 5000);


async function fetchData() {
  try {
    const response = await fetch(
      "https://api.tvmaze.com/search/shows?q=emmerdale",
    );
    if (!response.ok) {
      // Tarkistetaan, onnistuiko pyyntö (tilakoodi 200–299)
      throw new Error("HTTP-virhe! Tilakoodi: " + response.status);
    }
    const data = await response.json();
    console.log("Haettu data:", data);
    return data; // Palauttaa lupauksen, joka ratkeaa dataksi
  } catch (error) {
    console.error("Virhe datan haussa:", error);
  }
}
fetchData();
console.log("Tämä viesti tulostetaan ennen kuin data on haettu");

"use strict";
console.log("the script starts");

function synchronousFunction() {
  let number = 1;
  for (let i = 1; i < 100000; i++) {
    number += i;
    console.log("synchronousFunction running");
  }
  console.log("regular function complete", number);
}

async function asynchronousFunction() {
  // asynkroninen funktio määritellään async-avainsanalla
  console.log("asynchronous download begins");
  try {
    // virheenkäsittely: try/catch/finally
    const response = await fetch("http://127.0.0.1:3000/airport/00A"); // aloitetaan datan lataus; fetch palauttaa lupauksen, joka ratkeaa Response-olioksi
    const jsonData = await response.json(); // muunnetaan vastauksen JSON-data JavaScript-olioksi json()-metodilla
    console.log(jsonData.ICAO, jsonData.Name); // tulostetaan tulos konsoliin
  } catch (error) {
    console.log(error.message);
  } finally {
    // finally = suoritetaan joka tapauksessa, onnistui suoritus tai ei
    console.log("asynchronous load complete");
  }
}

synchronousFunction();
asynchronousFunction();

console.log("the script ends");