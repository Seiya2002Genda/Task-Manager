document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const input = form.querySelector("input[name='task']");
    const list = document.querySelector("ul");

    // =====================
    // 追加時チェック
    // =====================
    form.addEventListener("submit", (e) => {
        const value = input.value.trim();

        if (!value) {
            e.preventDefault();
            alert("Task cannot be empty");
            return;
        }
    });

    // =====================
    // 削除（フロント側）
    // =====================
    document.querySelectorAll(".delete-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const li = btn.closest("li");

            if (confirm("Delete this task?")) {
                li.remove();
            }
        });
    });

    // =====================
    // 完了トグル（追加機能）
    // =====================
    document.querySelectorAll("li").forEach(li => {
        li.addEventListener("click", () => {
            li.classList.toggle("completed");
        });
    });

});