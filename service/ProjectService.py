from model import ProjectModel, IssueModel


def getProjectKeyNames():
    projects = ProjectModel.findAll()
    for p in projects:
        del p["id"]
        del p["description"]
        del p["is_open"]

    return projects

def getProjectsForDashboard(userId):
    projects = ProjectModel.findProjectsByUserId(userId)

    for project in projects:
        # get issue counts
        issues = IssueModel.findIssuesByProjectId(project["id"])
        project["issues_total"] = len(issues)
        project["issues_open"] = len(
            [issue for issue in issues if int(issue["is_open"]) == 1])

        # get contributor usernames
        contributors = ProjectModel.findContributorsByProjectId(project["id"])
        project["contributors"] = list(
            map(lambda u: u["username"], contributors))

        # identify Admin
        project["admin"] = [cont for cont in contributors if int(
            cont["user_is_admin"]) == 1][0]

    return projects


def getProjectById(projectId):
    return ProjectModel.findProjectById(projectId)


def getProjectAdmin(projectId):
    return ProjectModel.findProjectAdmin(projectId)


def addProjectContributor(projectId, userId):
    ProjectModel.addContributor(projectId, userId)


def getProjectContributors(projectId):
    users = ProjectModel.findContributorsByProjectId(projectId)
    for user in users:
        del user["user_is_admin"]

    return users


def getOpenProjects():
    projects = ProjectModel.findProjectByIsOpenIsTrue()
    return sorted(projects, key=lambda p: p['key'])


def create(project):
    ProjectModel.create(project)
