from flask import Blueprint
from controllers.ProjectController import addContributor, getContributors, removeContributor, view, update, create, destroy, getProjects

# Initialise blueprint
projects = Blueprint("projects", __name__)

# Renders or Redirects to a Page
projects.route("/<int:id>", methods=["GET"])(view)
projects.route("/<int:id>", methods=["POST"])(update)
projects.route("/<int:id>/delete", methods=["GET"])(destroy)

# Returns JSON response
projects.route("", methods=["POST"])(create)
projects.route("", methods=["GET"])(getProjects)

projects.route("/<int:id>/contributors", methods=["GET"])(getContributors)
projects.route("/<int:id>/contributors", methods=["POST"])(addContributor)
projects.route("/<int:id>/contributors", methods=["DELETE"])(removeContributor)
