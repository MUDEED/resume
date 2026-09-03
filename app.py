from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def display_resume():
    data_dict = {
        "job_title": "Software Engineer",
        "skills": {
            "Languages & Frameworks": [
                "Python",
                "PySide/PyQt",
                "JavaScript",
                "HTML/CSS",
                "Flask",
                "Bash/Tcsh",
            ],
            "Databases & APIs": [
                "PostgreSQL",
                "MySQL",
                "SQLAlchemy",
                "JSON",
                "REST APIs",
                "Webhooks",
            ],
            "Libraries & Processing": [
                "NumPy",
                "ImageMagick",
                "FFmpeg",
                "OpenImageIO",
                "OpenColorIO",
            ],
            "Tools & Systems": ["Git", "GitHub", "GitLab", "Linux"],
            "DCC Software": [
                "Maya",
                "Blender",
                "Nuke",
                "Houdini",
                "RV",
                "After Effects",
            ],
        },
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
        "work_experience": [
            {
                "role": "Pipeline Engineer / Technical Director (TD)",
                "date": "2022 - 2026",
                "company": "The Monk Studios Co. Ltd.",
                "bullets": [
                    "<strong>Image & Media Pipelines: </strong>Built automated processing workflows using <strong>NumPy</strong> pixel arrays. "
                    "Handled EXR files with <strong>OpenImageIO (OIIO)</strong>. "
                    "Extracted frames from video using <strong>FFmpeg</strong> with custom <strong>OpenColorIO (OCIO)</strong> color-space conversions. ",
                    "<strong>Desktop UIs & Artist Support: </strong>Developed <strong>PySide2/PySide6</strong> GUI tools to monitor pipelines. "
                    "Supported artists across <strong>Maya, Nuke, Houdini, Blender, After Effects, Toon Boom, and RV</strong>. ",
                    "<strong>API & Review Automation: </strong>Designed <strong>Flask webhooks</strong> and REST APIs. "
                    "Synced <strong>PostgreSQL/SQLAlchemy</strong> backends with ShotGrid and SyncSketch. ",
                    "<strong>System Optimization & Editorial: </strong>Refactored legacy Python codebases for performance improvements. "
                    "Parsed <strong>OTIO</strong>, EDL, and XML timeline data. ",
                ],
            },
            {
                "role": "3D Animator",
                "date": "2021 - 2022",
                "company": "Lap Production Co. Ltd.",
                "bullets": [
                    "Animated 3D characters/props in Maya and built <strong>PyQt/Python</strong> tools to automate repetitive tasks and standardize media delivery pipelines."
                ],
            },
            {
                "role": "3D Animator (contract)",
                "date": "2019",
                "company": "World Learning Hub Asia Pacific Co. Ltd.",
                "bullets": [
                    "Created and animated 3D characters using Character Creator, iClone, and Blender."
                ],
            },
        ],
    }

    return render_template("resume.html", data_dict=data_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
