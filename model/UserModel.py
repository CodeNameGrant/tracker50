from cs50 import SQL

from model.utils import buildUserDisplayName

db = SQL("sqlite:///tracker50.db")


def findUsers():
    users = db.execute(
        'SELECT u.id, u.username, u.name AS displayName FROM users u')

    buildUserDisplayName(users)
    return users


def findUserByUsername(username):
    users = db.execute(
        'SELECT u.id, u.password, u.username, u.name AS displayName FROM users u WHERE LOWER(username) = ?', username.lower())

    buildUserDisplayName(users)

    return users[0] if len(users) != 0 else None


def findUserById(id):
    users = db.execute(
        'SELECT u.id, u.username, u.name AS displayName FROM users u WHERE id = ?', id)

    buildUserDisplayName(users)

    return users[0] if len(users) != 0 else None


def insertUser(username, password, name):
    return db.execute("INSERT INTO users (username, name, password) VALUES (?, ?, ?)",
                      username, name, password)
