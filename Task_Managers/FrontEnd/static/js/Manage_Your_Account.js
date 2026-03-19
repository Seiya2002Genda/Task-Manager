document.addEventListener("DOMContentLoaded", () => {

    const email = document.querySelector("p");

    email.addEventListener("click", () => {
        navigator.clipboard.writeText(email.innerText);
        alert("Email copied!");
    });

});