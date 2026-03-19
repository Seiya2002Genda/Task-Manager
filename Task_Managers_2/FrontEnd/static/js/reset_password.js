document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("resetPasswordForm");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");
    const resetButton = document.getElementById("resetButton");

    form.addEventListener("submit", (event) => {
        let isValid = true;

        passwordError.textContent = "";
        confirmPasswordError.textContent = "";

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

        resetButton.textContent = "Resetting...";
        resetButton.disabled = true;
    });
});