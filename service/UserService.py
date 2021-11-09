
from werkzeug.security import generate_password_hash

from model import UserModel


def getSortedUsers():
    return sorted(UserModel.findUsers(), key=lambda i: i['username'])


def usernameExists(username):
    return UserModel.findUserByUsername(username)


def getUserById(id):
    return UserModel.findUserById(id)


def getUserByUsername(username):
    return UserModel.findUserByUsername(username)


def createUser(username, password, name):
    return UserModel.insertUser(username, generate_password_hash(password), name)
