const cabinClass = prompt("Anna hyttiluokka (A/B/C).");
switch (cabinClass) {
  case "A":
    console.log("Yläkannen hytti, jossa on ikkuna.");
    break;
  case "B":
    console.log("Yläkannen hytti ilman ikkunaa.");
    break;
  case "C":
    console.log("Ikkunaton hytti autokannen alapuolella.");
    break;
  default:
    console.log("Virheellinen hyttiluokka.");
}

document.querySelector("#target").innerHTML = "toimiiko"
