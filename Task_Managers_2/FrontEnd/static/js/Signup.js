document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("signupForm");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");
    const signupButton = document.getElementById("signupButton");

    form.addEventListener("submit", (event) => {
        let isValid = true;

        emailError.textContent = "";
        passwordError.textContent = "";
        confirmPasswordError.textContent = "";

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
        } else if (password.value.trim().length < 6) {
            passwordError.textContent = "Password must be at least 6 characters.";
            isValid = false;
        }

        if (!confirmPassword.value.trim()) {
            confirmPasswordError.textContent = "Please confirm your password.";
            isValid = false;
        } else if (password.value !== confirmPassword.value) {
            confirmPasswordError.textContent = "Passwords do not match.";
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
            return;
        }

        signupButton.textContent = "Creating...";
        signupButton.disabled = true;
    });
});