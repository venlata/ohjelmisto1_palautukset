const kuvanen = "kuvanen1.jpeg";
document.querySelector("#logo").innerHTML = `<img src= '${kuvanen}' alt='kuva'/>`;

document.querySelector("p").innerHTML = "Sisältötekstiä";

document.querySelector("button").addEventListener("click", () =>{
    alert("HUHUU");
});