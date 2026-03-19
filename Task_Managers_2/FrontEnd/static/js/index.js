document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".primary-btn, .secondary-btn");
    buttons.forEach((button) => {
        button.addEventListener("mouseenter", () => {
            button.style.transform = "translateY(-2px)";
        });

        button.addEventListener("mouseleave", () => {
            button.style.transform = "translateY(0)";
        });
    });
});