from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from Task_Managers_2.Backend.ConnectDatabase import ConnectDatabase

task_bp = Blueprint("task", __name__)


def login_required():
    return "user_id" in session


@task_bp.route("/tasks", methods=["GET", "POST"])
def manage_task():
    if not login_required():
        flash("Please login first.", "error")
        return redirect(url_for("login.login"))

    user_id = session["user_id"]

    db = ConnectDatabase().connect()
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":
        task_text = request.form.get("task", "").strip()
        due_date = request.form.get("due_date", "").strip()

        if not task_text:
            flash("Task cannot be empty.", "error")
            cursor.close()
            db.close()
            return redirect(url_for("task.manage_task"))

        if len(task_text) > 255:
            flash("Task must be 255 characters or less.", "error")
            cursor.close()
            db.close()
            return redirect(url_for("task.manage_task"))

        if not due_date:
            flash("Please select a due date.", "error")
            cursor.close()
            db.close()
            return redirect(url_for("task.manage_task"))

        cursor.execute(
            """
            INSERT INTO tasks (user_id, task, status, due_date, progress)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (user_id, task_text, "pending", due_date, 0)
        )
        db.commit()

        flash("Task added successfully.", "success")
        cursor.close()
        db.close()
        return redirect(url_for("task.manage_task"))

    cursor.execute(
        """
        SELECT id, task, status, created_at, due_date, progress
        FROM tasks
        WHERE user_id=%s
        ORDER BY
            CASE WHEN status='pending' THEN 0 ELSE 1 END,
            due_date ASC,
            id DESC
        """,
        (user_id,)
    )
    tasks = cursor.fetchall()

    pending_count = sum(1 for task in tasks if task["status"] == "pending")
    done_count = sum(1 for task in tasks if task["status"] == "done")

    cursor.close()
    db.close()

    return render_template(
        "ManageTask.html",
        tasks=tasks,
        pending_count=pending_count,
        done_count=done_count
    )


@task_bp.route("/tasks/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    if not login_required():
        flash("Please login first.", "error")
        return redirect(url_for("login.login"))

    db = ConnectDatabase().connect()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE tasks SET status='done', progress=100 WHERE id=%s AND user_id=%s",
        (task_id, session["user_id"])
    )
    db.commit()

    cursor.close()
    db.close()

    flash("Task marked as completed.", "success")
    return redirect(url_for("task.manage_task"))


@task_bp.route("/tasks/pending/<int:task_id>", methods=["POST"])
def pending_task(task_id):
    if not login_required():
        flash("Please login first.", "error")
        return redirect(url_for("login.login"))

    db = ConnectDatabase().connect()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE tasks SET status='pending' WHERE id=%s AND user_id=%s",
        (task_id, session["user_id"])
    )
    db.commit()

    cursor.close()
    db.close()

    flash("Task moved back to pending.", "success")
    return redirect(url_for("task.manage_task"))


@task_bp.route("/tasks/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if not login_required():
        flash("Please login first.", "error")
        return redirect(url_for("login.login"))

    db = ConnectDatabase().connect()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s AND user_id=%s",
        (task_id, session["user_id"])
    )
    db.commit()

    cursor.close()
    db.close()

    flash("Task deleted successfully.", "success")
    return redirect(url_for("task.manage_task"))


@task_bp.route("/tasks/update_progress/<int:task_id>", methods=["POST"])
def update_progress(task_id):
    if not login_required():
        flash("Please login first.", "error")
        return redirect(url_for("login.login"))

    progress = request.form.get("progress", "0").strip()

    try:
        progress_value = int(progress)
    except ValueError:
        flash("Invalid progress value.", "error")
        return redirect(url_for("task.manage_task"))

    if progress_value < 0:
        progress_value = 0
    if progress_value > 100:
        progress_value = 100

    new_status = "done" if progress_value == 100 else "pending"

    db = ConnectDatabase().connect()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET progress=%s, status=%s
        WHERE id=%s AND user_id=%s
        """,
        (progress_value, new_status, task_id, session["user_id"])
    )
    db.commit()

    cursor.close()
    db.close()

    flash("Task progress updated.", "success")
    return redirect(url_for("task.manage_task"))