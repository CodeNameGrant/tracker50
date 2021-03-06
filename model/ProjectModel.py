from cs50 import SQL

from model.utils import buildUserDisplayName

db = SQL("sqlite:///tracker50.db")

def findAll():
    return db.execute("SELECT * FROM projects p")

def findProjectById(id):
    projects = db.execute(
        "SELECT p.id, p.key, p.name, p.description, p.is_open, u.username, u.name AS displayName FROM projects p"
        " JOIN users_projects up ON up.project_id = p.id"
        " JOIN users u ON up.user_id = u.id"
        " WHERE p.id = ?"
        "", id
    )

    buildUserDisplayName(projects)

    return projects[0] if len(projects) != 0 else None


def findProjectAdmin(id):
    admins = db.execute(
        "SELECT u.id, u.username, u.name AS displayName FROM users u"
        " JOIN users_projects up ON up.user_id = u.id"
        " WHERE up.user_is_admin = 1 AND up.project_id = ?", id
    )

    buildUserDisplayName(admins)

    return admins[0] if len(admins) != 0 else None


def findProjectUsers(projectId):
    return db.execute(
        "SELECT * from users u"
        " JOIN users_projects up ON u.id = up.user_id"
        " WHERE up.project_id = ?",
        projectId
    )


def findProjectByIsOpenIsTrue():
    return db.execute(
        "SELECT p.id, p.name, p.key FROM projects p"
        " WHERE p.is_open = 1"
    )


def findContributorsByProjectId(id):
    users = db.execute(
        "SELECT u.id, u.username, u.name AS displayName, up.user_is_admin FROM users u"
        " JOIN users_projects up ON u.id = up.user_id"
        " WHERE up.project_id = ?",
        id
    )

    buildUserDisplayName(users)
    return users


def findProjectsByUserId(userId):
    return db.execute(
        "SELECT * from projects p"
        " JOIN users_projects up ON p.id = up.project_id"
        " WHERE up.user_id = ?",
        userId
    )


def create(project):
    projectId = db.execute(
        "INSERT INTO projects(key, name, description, is_open) VALUES (?, ?, ?, ?)",
        project["key"].upper(), project["name"], project["description"], 1
    )

    db.execute(
        "INSERT INTO users_projects(project_id, user_id, user_is_admin) VALUES (?, ?, ?)",
        projectId, project["adminId"], 1
    )


def linkUserToProject(projectId, userId):
    return db.execute(
        "INSERT INTO users_projects(project_id, user_id) VALUES (?, ?)",
        projectId, userId
    )

def deleteProject(id):
    db.execute("DELETE FROM projects where id = ?", id)


def updateDescriptionByProjectId(id, description):
    db.execute(
            "UPDATE projects SET description = ? WHERE id = ?", 
            description,id
        )

def linkUserToProject(projectId, userId):
    db.execute("DELETE FROM users_projects WHERE project_id = ? AND user_id = ?", projectId, userId)

def unlinkProjectUsers(projectId):
    db.execute("DELETE FROM users_projects WHERE project_id = ?", projectId)


def reassignIssues(projectId, currentUserId, futureUserId):
    db.execute(
        "UPDATE issues SET" +
        " assignee_id = ?" +
        " WHERE project_id = ? AND assignee_id = ? AND is_open = 1",
        futureUserId, projectId, currentUserId
    )