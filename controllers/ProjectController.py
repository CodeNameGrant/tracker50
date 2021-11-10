import json

from itertools import filterfalse
from flask import render_template, request, session, Response

from service import ProjectService, IssueService, UserService
from service.AuthService import require_auth


@require_auth
def getProjects():
    projects = []   # default value

    if (request.args.get('isOpen') is not None):
        projects = ProjectService.getOpenProjects()

    return Response(response=json.dumps(projects), status=200)


@require_auth
def view(id):
    print("viewProject", id)

    userId = session["user_id"]

    project = ProjectService.getProjectById(id)
    projectAdmin = ProjectService.getProjectAdmin(id)
    project["admin"] = projectAdmin
    project["userIsAdmin"] = projectAdmin["id"] == userId

    contributors = ProjectService.getProjectContributors(id)
    users = UserService.getSortedUsers()

    # Get users that are not linked to the project
    cUsernames = [c['username'] for c in contributors]
    nonContributors = filterfalse(lambda u: u["username"] in cUsernames, users)

    # get issues and sort them, Open at the top
    issues = IssueService.getIssuesByProjectId(id)
    issues = sorted(issues, key=lambda i: i['is_open'], reverse=True)

    return render_template("projects/view.html",
                           project=project,
                           issues=issues,
                           contributors=contributors,
                           users=nonContributors)


@require_auth
def create():
    project = {
        "key": request.json['key'],
        "name": request.json['name'],
        "description": request.json['description'],
        "adminId": session["user_id"]
    }

    try:
        ProjectService.create(project)
    except:
        return Response(response=json.dumps({"message": "Project Key already exists"}), status=400)

    return Response(status=201)


@require_auth
def destroy(id):
    print("deleteProject", id, request.method)
    return render_template("projects/index.html")


@require_auth
def getContributors(id):
    users = ProjectService.getProjectContributors(id)
    return Response(response=json.dumps(users), status=200)


@require_auth
def addContributor(id):
    userId = session["user_id"]

    contributorId = int(request.json["contributorId"])

    projectAdmin = ProjectService.getProjectAdmin(id)
    if projectAdmin["id"] != userId:
        return Response(response=json.dumps({"message": "Only project admin can add contributors"}), status=400)

    try:
        ProjectService.addProjectContributor(id, contributorId)
        return Response(response=json.dumps([UserService.getUserById(contributorId)]), status=200)

    except:
        return Response(response=json.dumps({"message": "User is already a contributor of this project"}), status=400)
