document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {
        const email = form.email.value.trim();

        if (!email) {
            e.preventDefault();
            alert("Enter email");
            return;
        }

        alert("OTP is being sent...");
    });

});