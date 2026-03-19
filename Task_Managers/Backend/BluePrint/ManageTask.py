from flask import Blueprint, render_template, request, session
from Task_Managers.Backend.ConnectDatabase import ConnectDatabase

task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["GET", "POST"])
def manage_task():
    db = ConnectDatabase().connect()
    cursor = db.cursor(dictionary=True)

    user_id = session.get("user_id")

    if request.method == "POST":
        task = request.form["task"]

        cursor.execute(
            "INSERT INTO tasks (user_id, task, status) VALUES (%s, %s, %s)",
            (user_id, task, "pending")
        )
        db.commit()

    cursor.execute("SELECT * FROM tasks WHERE user_id=%s", (user_id,))
    tasks = cursor.fetchall()

    return render_template("ManageTask.html", tasks=tasks)

@task_bp.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    db = ConnectDatabase().connect()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE tasks SET status='done' WHERE id=%s",
        (task_id,)
    )
    db.commit()

    return redirect("/tasks")