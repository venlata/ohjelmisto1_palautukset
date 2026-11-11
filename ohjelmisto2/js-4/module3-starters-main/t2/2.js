// ul id="target"
//    li
//    li

const targee = document.getElementById("target");

const liOne = document.createElement("li");
liOne.innerHTML = `<li>First item</li>`;

const liTwo = document.createElement("li");
liTwo.innerHTML = `<li>Second item</li>`;

const liThree = document.createElement("li");
liThree.innerHTML = `<li>Third item</li>`;

targee.appendChild(liOne);
targee.appendChild(liTwo);
targee.appendChild(liThree);

liTwo.classList.add("my-item");

// const second = document.getElementsByTagName("li")[1];

// second.classList.add("my-item");
// nuh uh
