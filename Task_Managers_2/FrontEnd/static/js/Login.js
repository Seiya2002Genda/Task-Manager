document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const loginButton = document.getElementById("loginButton");

    form.addEventListener("submit", (event) => {
        let isValid = true;

        emailError.textContent = "";
        passwordError.textContent = "";

        if (!email.value.trim()) {
            emailError.textContent = "Email is required.";
            isValid = false;
        } else if (!/^\S+@\S+\.\S+$/.test(email.value.trim())) {
            emailError.textContent = "Enter a valid email address.";
            isValid = false;
        }

        if (!password.value.trim()) {
            passwordError.textContent = "Password is required.";
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
            return;
        }

        loginButton.textContent = "Logging in...";
        loginButton.disabled = true;
    });
});