'use strict';
const names = ['John', 'Paul', 'Jones'];

const targee = document.getElementById("target");

for (let name of names) {
    targee.appendChild(document.createElement("li")).innerHTML = `<li>${name}</li>
    `;
}