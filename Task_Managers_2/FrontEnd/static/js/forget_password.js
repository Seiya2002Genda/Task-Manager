document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("forgetForm");
    const email = document.getElementById("email");
    const emailError = document.getElementById("emailError");
    const sendOtpButton = document.getElementById("sendOtpButton");

    form.addEventListener("submit", (event) => {
        let isValid = true;
        emailError.textContent = "";

        if (!email.value.trim()) {
            emailError.textContent = "Email is required.";
            isValid = false;
        } else if (!/^\S+@\S+\.\S+$/.test(email.value.trim())) {
            emailError.textContent = "Enter a valid email address.";
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
            return;
        }

        sendOtpButton.textContent = "Sending OTP...";
        sendOtpButton.disabled = true;
    });
});