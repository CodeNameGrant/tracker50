from flask import redirect, request, session
from cs50 import SQL
from service.AuthService import require_anon, require_auth
from service import UserService
from werkzeug.security import check_password_hash


@require_anon
def register():
    """Register user"""

    # validate username exists
    username = request.form.get("username")
    if not username:
        return redirect("/?error")

    # validate username not in db
    if UserService.usernameExists(username):
        return redirect("/?error")

    # validate passwords provided
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    if not password or not confirm_password:
        return redirect("/?error")

    # validate passwords match
    if password != confirm_password:
        return redirect("/?error")

    # Add user to DB
    new_user_id = UserService.createUser(
        username, password, request.form.get('name'))

    # Log user in
    session.clear()
    session["user_id"] = new_user_id

    # redirect to dashboard
    return redirect("/dashboard")


@require_anon
def login():
    """Login user"""

    # validate username exists
    username = request.form.get("username")
    if not username:
        return redirect("/?error-user")

    password = request.form.get("password")
    if not password:
        return redirect("/?error-pass")

    # get user by name
    user = UserService.getUserByUsername(username)
    if user is None or not check_password_hash(user["password"], password):
        return redirect("/?error-user-pass")

    # Log user in
    session.clear()
    session["user_id"] = user["id"]

    # redirect to dashboard
    return redirect("/dashboard")


@require_auth
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
