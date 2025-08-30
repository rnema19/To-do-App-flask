from flask import request, Blueprint,render_template,session,flash,url_for,redirect
from app.models import Task
from app import db

task_bp = Blueprint("task",__name__)

@task_bp.route("/",methods=["GET"])
def view_tasks():
    if "user" not in session:
        flash(message="Not logged in!",category="info")
        return redirect(url_for("auth.login"))
    
    tasks = Task.query.all()
    return render_template("tasks.html",tasks=tasks)

@task_bp.route("/edit/<int:id>",methods=["POST"])
def edit_task(id):
    task = Task.query.get(id)
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            db.session.delete(task)
            db.session.commit()
            flash(message="Task completed successfully so removed from list!",category="success")
    db.session.commit()
    flash(message="Task edited successfully!",category="success")
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/add",methods=["POST"])
def add_task():
    if "user" not in session:
        flash(message="Not logged in!",category="info")
        return redirect(url_for("auth.login"))
    title = request.form.get("title")
    if title:
        new_task = Task(title=title,status="Pending")
        db.session.add(new_task)
        db.session.commit()
        flash(message="Task added successfully!",category="success")
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/delete/<int:id>",methods=["POST"])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash(message="Task removed successfully!",category="success")
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/clear",methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash(message="All Tasks removed successfully!",category="success")
    return redirect(url_for("task.view_tasks"))
                   
            
    
