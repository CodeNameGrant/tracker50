from flask import Blueprint
from controllers.AuthController import register, login, logout

# Initialise blueprint
AuthService = Blueprint("AuthService", __name__)

# Renders or Redirects to a Page
AuthService.route("/register", methods=["POST"])(register)
AuthService.route("/login", methods=["POST"])(login)
AuthService.route("/logout", methods=["GET"])(logout)
