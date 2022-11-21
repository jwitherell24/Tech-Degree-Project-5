from flask import (render_template, redirect,
                   url_for, request)
from models import db, Project, app
import datetime


@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)


@app.route("/skills")
def skills():
    projects = Project.query.all()
    return render_template("skills.html", projects=projects)


@app.route("/projects/about")
def about():
    projects = Project.query.all()
    return render_template("about.html", projects=projects)


@app.route("/projects/new", methods=["GET", "POST"])
def create_project():
    projects = Project.query.all()
    if request.form:
        split_date = request.form["date"].split("-")
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        clean_date = datetime.date(year, month, day)
        new_project = Project(title=request.form["title"],
                              date_finished=clean_date,
                              skills_used=request.form["skills"],
                              description=request.form["description"],
                              github_link=request.form["url"])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("createproject.html", projects=projects)


@app.route("/projects/<id>")
def projects(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template("projects.html", projects=projects, project=project)


@app.route("/projects/<id>/edit", methods=["GET", "POST"])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        split_date = request.form["date"].split("-")
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        clean_date = datetime.date(year, month, day)
        project.title = request.form["title"]
        project.date_finished = clean_date 
        project.skills_used = request.form["skills"]
        project.description = request.form["description"]
        project.github_link = request.form["url"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("editproject.html", projects=projects, project=project)


@app.route("/projects/<id>/delete")
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template("404.html", msg=error, projects=projects), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
    