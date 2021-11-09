import markdown

from flask import Flask, render_template, redirect, session
from service.AuthService import require_auth
from flask_session import Session

from routes.auth_bp import AuthService
from routes.projects_bp import projects
from routes.issues_bp import issues

from service import ProjectService, IssueService

app = Flask(__name__)
app.config.from_object('config')

# Register Blueprints
app.register_blueprint(AuthService, url_prefix="/")
app.register_blueprint(projects, url_prefix="/projects")
app.register_blueprint(issues, url_prefix="/issues")

# Init. Session
Session(app)


# Ensure responses aren't caches
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Index access to application"""

    if "user_id" in session:
        return redirect("/dashboard")

    with open('README.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    return render_template("index.html", readme=html)


@app.route("/dashboard")
@require_auth
def dashboard():
    """Display current projects/issues for the user"""

    userId = session["user_id"]
    projects = ProjectService.getProjectsForDashboard(userId)
    issues = IssueService.getOpenIssuesByUserId(userId)

    return render_template("dashboard.html",
                           projects=projects,
                           issues=issues)
