from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def display_resume():
    data_dict = {
        "job_title": "Python Developer",
        "skills": [
            "Python",
            "PySide/PyQt",
            "PostgreSQL/MySQL",
            "SQLAlchemy",
            "HTML/CSS",
            "JavaScript",
            "JSON",
            "Git - GitHub/GitLab",
            "Linux - bash/tcsh",
        ],
        "languages": ["Thai", "English"],
        "educations": {
            "Bachelor of Science Multimedia and Animation Technology": [
                "Mahanakorn University of Technology",
                "2016 - 2018",
            ],
            "Diploma in Information Technology": [
                "Intrachai Commercial College",
                "2013 - 2015",
            ],
        },
    }

    return render_template(
        "resume.html",
        data_dict=data_dict,
    )
