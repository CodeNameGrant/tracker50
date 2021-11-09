def buildUserDisplayName(data):
    for item in data:
        item["userDisplayName"] = item["username"]
        if item["displayName"] is not None:
            item["userDisplayName"] += f" ({item['displayName']})"
            del item["displayName"]


def buildIssueKey(data):
    for issue in data:
        issue["key"] = issue["key"] + "-" + str(issue["id"])
