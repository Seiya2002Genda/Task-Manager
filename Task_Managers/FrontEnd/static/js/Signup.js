document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {

        const email = form.email.value.trim();
        const password = form.password.value.trim();

        if (!email || !password) {
            e.preventDefault();
            alert("All fields required");
            return;
        }

        if (password.length < 6) {
            e.preventDefault();
            alert("Password must be at least 6 characters");
            return;
        }

        form.querySelector("button").innerText = "Creating...";
    });

});