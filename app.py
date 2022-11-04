from flask import (render_template, redirect,
                   url_for, request)
from models import db, Project, app


@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)


@app.route("/projects/new", methods=["GET", "POST"])
def create_project():
    if request.form:
        new_project = Project(title=request.form["title"],
                              date_finished=request.form["date finished"],
                              skills_used=request.form["skills used"],
                              description=request.form["description"])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("createproject.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")