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

