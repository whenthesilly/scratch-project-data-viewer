import requests

projId = input("Project id?\n")

response = requests.get(str("https://scratchdb.lefty.one/v2/project/info/id/" + projId))
projectInfo = response.json()

print("\n\ntitle:\n", projectInfo["title"])

stats = projectInfo["statistics"]
print("\nstats:\n")
print(" views:\n", stats["views"])
print(" loves:\n", stats["loves"])
print(" favouites:\n", stats["favorites"])
print(" comments:\n", stats["comments"])


print("\ninstructions:\n", projectInfo["instructions"])
print("\nnotes and credits:\n", projectInfo["description"])

projhistory = projectInfo["times"]
print("\ncreated:\n", projhistory["created"])
print("modified:\n", projhistory["modified"])
print("shared:\n", projhistory["shared"])
print("last updated:\n", projectInfo["last_updated"])

remixes = projectInfo["remix"]
print("\nremix parent:\n", remixes["parent"])
print("root remix:\n", remixes["root"])
