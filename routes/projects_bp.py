from flask import Blueprint
from controllers.ProjectController import addContributor, getContributors, view, create, destroy, getProjects

# Initialise blueprint
projects = Blueprint("projects", __name__)

# TODO
projects.route("/<int:id>", methods=["DELETE"])(destroy)

# Renders or Redirects to a Page
projects.route("/<int:id>", methods=["GET"])(view)

# Returns JSON response
projects.route("", methods=["POST"])(create)
projects.route("", methods=["GET"])(getProjects)

projects.route("/<int:id>/contributors", methods=["GET"])(getContributors)
projects.route("/<int:id>/contributors", methods=["POST"])(addContributor)