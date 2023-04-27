# i didnt finish this clearly

# All data from scratchDB by datonelefty
import requests

projId = input("Project id?\n>>> ")

response = requests.get(str("https://scratchdb.lefty.one/v3/project/info/" + projId))
projectInfo = response.json()
# Below line was used for debugging
# print(projectInfo)

print("\nProject Title:", projectInfo["title"])
print("Is public:", str(projectInfo["public"]))  # probably useless nowadays

username = projectInfo["username"]
print("\nAuthor's Username:", username)

print("\nInstructions:", projectInfo["instructions"])
print("\nNotes and Creds:", projectInfo["description"])
print("\nComments disallowed:", str(projectInfo["comments_allowed"]))

stats = projectInfo["statistics"]
print("\nLoves:", str(stats["loves"]))
print("Faves:", str(stats["favorites"]))
print("Views:", str(stats["views"]))
print("Comments:", str(stats["comments"]))

metadata = projectInfo["metadata"]
print("\nVersion:", metadata["version"])
print("Block count:", metadata["blocks"])
print("Variable count:", metadata["variables"])
print("Costume count:", metadata["costumes"])


remix = projectInfo["remix"]
print("\nRemix parent:", str(remix["parent"]))
print("Remix root:", str(remix["root"]))
