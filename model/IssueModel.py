from cs50 import SQL

from model.utils import buildIssueKey, buildUserDisplayName

db = SQL("sqlite:///tracker50.db")

def findAll():
    issues = db.execute(
        "SELECT p.key, i.id, i.title, i.description, i.is_open, u.username, u.name AS displayName FROM issues i" +
        " JOIN users u ON u.id = i.assignee_id" +
        " JOIN projects p ON p.id = i.project_id"
    )

    buildUserDisplayName(issues)
    buildIssueKey(issues)
    return issues

def findIssuesByProjectId(projectId):
    issues = db.execute(
        "SELECT p.key, i.id, i.title, i.description, i.is_open, u.username, u.name AS displayName FROM issues i" +
        " JOIN users u ON u.id = i.assignee_id" +
        " JOIN projects p ON p.id = i.project_id" +
        " WHERE i.project_id = ?", projectId
    )

    buildUserDisplayName(issues)
    buildIssueKey(issues)
    return issues


def findIssuesByUserId(userId):
    issues = db.execute(
        "SELECT p.key, i.id, i.title, i.description, i.is_open, u.username, u.name AS displayName FROM issues i" +
        " JOIN users u ON u.id = i.assignee_id" +
        " JOIN projects p ON p.id = i.project_id" +
        " WHERE u.id = ?", userId
    )

    buildUserDisplayName(issues)
    buildIssueKey(issues)
    return issues


def findOpenIssuesByUserId(userId):
    issues = db.execute(
        "SELECT p.key, i.id, i.title, i.description, i.is_open, u.username, u.name AS displayName FROM issues i" +
        " JOIN users u ON u.id = i.assignee_id" +
        " JOIN projects p ON p.id = i.project_id" +
        " WHERE i.is_open = 1 AND u.id = ?", userId
    )

    buildUserDisplayName(issues)
    buildIssueKey(issues)
    return issues


def findAll():
    issues = db.execute(
        "SELECT DISTINCT p.key, i.id, i.title, i.description, i.is_open, u.username, u.name AS displayName FROM issues i" +
        " JOIN users u ON u.id = i.assignee_id" +
        " JOIN projects p ON p.id = i.project_id" +
        " JOIN users_projects up ON up.user_id = u.id"
    )

    buildUserDisplayName(issues)
    buildIssueKey(issues)
    return issues


def create(issue):
    db.execute(
        "INSERT INTO issues(title, description, assignee_id, project_id) VALUES (?, ?, ?, ?)",
        issue["title"], issue["description"], issue["assigneeId"], issue["projectId"]
    )
