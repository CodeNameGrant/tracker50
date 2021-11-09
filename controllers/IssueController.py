from flask import render_template, request, Response
from service.AuthService import require_auth

from service import IssueService


@require_auth
def find():
    print('issues-find')

    query = request.args.get("q")
    issues = [] if query is None else IssueService.searchIssues(query)

    return render_template("issues/find.html", issues=issues)


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
