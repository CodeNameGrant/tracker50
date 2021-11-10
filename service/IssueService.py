
from model import IssueModel


def getIssues():
    return IssueModel.findAll()


def getIssuesByUserId(userId):
    return IssueModel.findIssuesByUserId(userId)


def getIssuesByProjectId(id):
    return IssueModel.findIssuesByProjectId(id)


def getOpenIssuesByUserId(userId):
    return IssueModel.findOpenIssuesByUserId(userId)


def create(issue):
    IssueModel.create(issue)


def removeIssuesByProjectId(id):
    IssueModel.deleteIssuesByProjectId(id)