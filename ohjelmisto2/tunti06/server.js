const haeLottorivi =  () => {
    const response = await fetch("/viikon-lottorivi");
    console.log("response", response);
};

haeLottorivi();

document.querySelector("h1").innerText += data.join("👹")