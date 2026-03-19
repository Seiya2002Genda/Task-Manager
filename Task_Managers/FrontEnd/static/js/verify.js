document.addEventListener("DOMContentLoaded", () => {

    const input = document.querySelector("input[name='otp']");
    const form = document.querySelector("form");

    // 数字のみ
    input.addEventListener("input", () => {
        input.value = input.value.replace(/\D/g, "");
    });

    form.addEventListener("submit", (e) => {
        if (input.value.length !== 6) {
            e.preventDefault();
            alert("OTP must be 6 digits");
        }
    });

});