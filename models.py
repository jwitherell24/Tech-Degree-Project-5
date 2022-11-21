from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project_portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Project Title", db.String())
    date_finished = db.Column("Date Finished", db.Date)
    skills_used = db.Column("Skills Used", db.Text)
    description = db.Column("Project Description", db.Text)
    github_link = db.Column("GitHub Link", db.Text)
    
    def __repr__(self):
        return f"""<Project:
                Title: {self.title}
                Date Finished: {self.date_finished}
                Skills Used: {self.skills_used}
                Description: {self.description}
                GitHub Link: {self.github_link}"""
                