import requests

github_user_name = input("Provide the GitHub username : ")
print(f"Hello, {github_user_name}!")


url = f"https://api.github.com/users/{github_user_name}/events"
# print(f"Fetching events for {github_user_name}...")

response = requests.get(url)
print("fetching...")

if response.status_code == 200:
    events = response.json()

    if len(events) == 0:
        print(f"No Recent Activity found for you dear: {github_user_name}")
    else:
        print("Here are your recent activity Items:")
    for event in events:
        repo_name = event["repo"]["name"]
        event_type = event["type"]

        if event_type == "PushEvent":
            commit_count = len(event["payload"].get("commits", []))
            print(
                f"- Pushed {commit_count} commit{'s' if commit_count != 1 else ''} to {repo_name}"
            )
        elif event_type == "IssuesEvent":
            action = event["payload"].get("action", "")
            if action == "opened":
                print(f"- Opened a new issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
else:
    print(f"No Such username: {response.status_code}")
