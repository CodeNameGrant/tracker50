from flask import Blueprint
from controllers.IssueController import find, save, destroy

# Initialise blueprint
issues = Blueprint("issues", __name__)

# Renders or Redirects to a Page
issues.route("", methods=["GET"])(find)
issues.route("", methods=["POST"])(save)
issues.route("/<int:id>", methods=["DELETE"])(destroy)
