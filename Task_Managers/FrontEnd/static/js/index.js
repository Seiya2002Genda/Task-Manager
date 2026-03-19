document.addEventListener("DOMContentLoaded", () => {
    console.log("Index Ready");

    const links = document.querySelectorAll("a");

    links.forEach(link => {
        link.addEventListener("mouseenter", () => {
            link.style.opacity = "0.7";
        });

        link.addEventListener("mouseleave", () => {
            link.style.opacity = "1";
        });
    });
});