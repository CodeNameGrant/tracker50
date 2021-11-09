
from model import IssueModel


def getIssues():
    return IssueModel.findAll()


def getIssuesByUserId(userId):
    return IssueModel.findIssuesByUserId(userId)


def getIssuesByProjectId(id):
    return IssueModel.findIssuesByProjectId(id)


def getOpenIssuesByUserId(userId):
    return IssueModel.findOpenIssuesByUserId(userId)


def searchIssues(query):
    issues = IssueModel.findAll()
    matches = []
    print("query", query)

    # split query
    queryList = query.split(" ")

    for issue in issues:
        if (listContainsPartialString(queryList, issue["key"]) or
            listContainsPartialString(queryList, issue["title"]) or
            listContainsPartialString(queryList, issue["description"]) or
                listContainsPartialString(queryList, issue["userDisplayName"])):
            matches.append(issue)

    return matches


def create(issue):
    IssueModel.create(issue)


def listContainsPartialString(list, str):
    for item in list:
        if item.lower() in str.lower():
            return True

    return False
