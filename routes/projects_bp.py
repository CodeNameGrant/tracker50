from flask import Blueprint
from controllers.ProjectController import addContributor, getContributors, removeContributor, view, update, create, destroy, getProjects

# Initialise blueprint
projects = Blueprint("projects", __name__)

# TODO
projects.route("/<int:id>", methods=["DELETE"])(destroy)

# Renders or Redirects to a Page
projects.route("/<int:id>", methods=["GET"])(view)
projects.route("/<int:id>", methods=["POST"])(update)

# Returns JSON response
projects.route("", methods=["POST"])(create)
projects.route("", methods=["GET"])(getProjects)

projects.route("/<int:id>/contributors", methods=["GET"])(getContributors)
projects.route("/<int:id>/contributors", methods=["POST"])(addContributor)
projects.route("/<int:id>/contributors", methods=["DELETE"])(removeContributor)
