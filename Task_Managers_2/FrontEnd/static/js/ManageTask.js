document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById("taskForm");
    const taskInput = document.getElementById("taskInput");
    const dueDateInput = document.getElementById("dueDateInput");
    const taskError = document.getElementById("taskError");
    const taskSubmitButton = document.getElementById("taskSubmitButton");
    const searchInput = document.getElementById("taskSearch");
    const taskItems = document.querySelectorAll(".task-item");
    const emptySearchState = document.getElementById("emptySearchState");

    if (taskForm) {
        taskForm.addEventListener("submit", (event) => {
            taskError.textContent = "";

            if (!taskInput.value.trim()) {
                taskError.textContent = "Task cannot be empty.";
                event.preventDefault();
                return;
            }

            if (taskInput.value.trim().length > 255) {
                taskError.textContent = "Task must be 255 characters or less.";
                event.preventDefault();
                return;
            }

            if (!dueDateInput.value.trim()) {
                taskError.textContent = "Please select a due date.";
                event.preventDefault();
                return;
            }

            taskSubmitButton.textContent = "Adding...";
            taskSubmitButton.disabled = true;
        });
    }

    document.querySelectorAll(".delete-form").forEach((form) => {
        form.addEventListener("submit", (event) => {
            const confirmed = confirm("Are you sure you want to delete this task?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    document.querySelectorAll(".progress-form").forEach((form) => {
        const slider = form.querySelector(".progress-slider");
        const taskItem = form.closest(".task-item");
        const progressFill = taskItem.querySelector(".progress-fill");
        const progressLabel = taskItem.querySelector(".progress-info span:last-child");

        if (slider && progressFill && progressLabel) {
            slider.addEventListener("input", () => {
                const value = slider.value;
                progressFill.style.width = `${value}%`;
                progressLabel.textContent = `${value}%`;
            });
        }
    });

    if (searchInput) {
        searchInput.addEventListener("input", () => {
            const query = searchInput.value.trim().toLowerCase();
            let visibleCount = 0;

            taskItems.forEach((item) => {
                const text = item.dataset.taskText || "";
                const shouldShow = text.includes(query);
                item.style.display = shouldShow ? "flex" : "none";
                if (shouldShow) {
                    visibleCount += 1;
                }
            });

            if (emptySearchState) {
                emptySearchState.classList.toggle("hidden", visibleCount !== 0);
            }
        });
    }
});