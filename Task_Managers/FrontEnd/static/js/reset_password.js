document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {

        const password = form.password.value;

        if (password.length < 6) {
            e.preventDefault();
            alert("Password must be at least 6 characters");
            return;
        }

        alert("Password updated successfully");
    });

});