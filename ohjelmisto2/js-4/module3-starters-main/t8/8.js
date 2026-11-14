const nOne = document.getElementById("num1");

const nTwo = document.getElementById("num2");

const select = document.getElementById("operation");

const calculate = document.getElementById("start");

const result = document.getElementById("result");

// select.addEventListener ("change", function () {
//     if (select.value === "add") {
//         result.textContent = parseInt(nOne.value) + parseInt(nTwo.value);
//     } 
//     else if (select.value === "sub") {
//         result.textContent = parseInt(nOne.value) - parseInt(nTwo.value);
//     } 
//     else if (select.value === "multi") {
//         result.textContent = parseInt(nOne.value) * parseInt(nTwo.value);
//     } 
//     else if (select.value === "div") {
//         result.textContent = parseInt(nOne.value) / parseInt(nTwo.value);
//     }
// });


calculate.addEventListener("click", function () {
    if (select.value === "add") {
        result.textContent = parseInt(nOne.value) + parseInt(nTwo.value);
    } 
    else if (select.value === "sub") {
        result.textContent = parseInt(nOne.value) - parseInt(nTwo.value);
    } 
    else if (select.value === "multi") {
        result.textContent = parseInt(nOne.value) * parseInt(nTwo.value);
    } 
    else if (select.value === "div") {
        result.textContent = parseInt(nOne.value) / parseInt(nTwo.value);
    }
    console.log(result.textContent);
});