from itertools import filterfalse
from flask import render_template, request, Response
from service.AuthService import require_auth

from service import IssueService, ProjectService


@require_auth
def find():
    print('issues-find')

    issues = IssueService.getIssues()

    isOpen = request.args.get("isOpen")
    if (isOpen is not None):
        issues = filterfalse(lambda i: int(i["is_open"]) != int(isOpen), issues)

    project = request.args.get("project")
    if (project is not None):
        issues = filterfalse(lambda i: project.lower() not in i["key"].lower(), issues)

    assignee = request.args.get("assignee")
    if (assignee is not None):
        issues = filterfalse(lambda i: assignee.lower() not in i["userDisplayName"].lower(), issues)

    query = request.args.get("q")
    if (query is not None):
        queryList = query.lower().split(" ")
        # TODO:
        

    return render_template("issues/find.html", 
                            issues=issues, 
                            projects=ProjectService.getProjectKeyNames())


@require_auth
def save():

    issue = {
        "projectId": int(request.json['projectId']),
        "assigneeId": int(request.json['assigneeId']),
        "title": request.json['title'],
        "description": request.json['description'],
    }

    try:
        IssueService.create(issue)
        return Response(status=201)

    except:
        return Response(status=400)


@require_auth
def destroy(id):
    print("deleteIssues", id, request.method)
    return render_template("issues/index.html")
