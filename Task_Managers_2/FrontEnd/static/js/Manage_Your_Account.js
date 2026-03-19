document.addEventListener("DOMContentLoaded", () => {
    const copyEmailButton = document.getElementById("copyEmailButton");
    const emailValue = document.getElementById("emailValue");

    if (copyEmailButton && emailValue) {
        copyEmailButton.addEventListener("click", async () => {
            try {
                await navigator.clipboard.writeText(emailValue.textContent.trim());
                copyEmailButton.textContent = "Copied!";
                setTimeout(() => {
                    copyEmailButton.textContent = "Copy Email";
                }, 1500);
            } catch (error) {
                alert("Failed to copy email.");
            }
        });
    }
});