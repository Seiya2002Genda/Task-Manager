document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {
        const email = form.email.value.trim();
        const password = form.password.value.trim();

        if (!email || !password) {
            e.preventDefault();
            alert("Please fill all fields");
            return;
        }

        if (!email.includes("@")) {
            e.preventDefault();
            alert("Invalid email format");
            return;
        }

        // ローディング表示
        form.querySelector("button").innerText = "Logging in...";
    });

});