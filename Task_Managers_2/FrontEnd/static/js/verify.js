document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("verifyForm");
    const otp = document.getElementById("otp");
    const otpError = document.getElementById("otpError");
    const verifyButton = document.getElementById("verifyButton");

    otp.addEventListener("input", () => {
        otp.value = otp.value.replace(/\D/g, "").slice(0, 6);
    });

    form.addEventListener("submit", (event) => {
        otpError.textContent = "";

        if (!otp.value.trim()) {
            otpError.textContent = "OTP is required.";
            event.preventDefault();
            return;
        }

        if (otp.value.trim().length !== 6) {
            otpError.textContent = "OTP must be 6 digits.";
            event.preventDefault();
            return;
        }

        verifyButton.textContent = "Verifying...";
        verifyButton.disabled = true;
    });
});