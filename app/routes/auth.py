from flask import request, Blueprint,render_template,session,flash,url_for, redirect

auth_bp = Blueprint('auth', __name__)

User_credentials = {
    "username" : "admin",
    "password" : "1234" 
}

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password") 
        if username==User_credentials["username"] and password==User_credentials["password"]:
            session["user"] = username
            flash(message="Details matched, login successful!",category="success")
            return redirect(url_for("task.view_tasks"))
        else:
            flash(message="Details are invalid! Please try again",category="danger")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user",None)
    flash(message="Logout successfull, enter details to login again!",category="info")
    return redirect(url_for("auth.login"))
            