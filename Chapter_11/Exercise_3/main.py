import json
import requests

URL = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(URL)
tasks = response.json()

completed = []
incomplete = []

for task in tasks:
    if task["completed"]:
        completed.append(task)
    else:
        incomplete.append(task)

with open("completed_tasks.json", "w") as f:
    json.dump(completed, f, separators=(",", ":"))

with open("incomplete_tasks.json", "w") as f:
    json.dump(incomplete, f, separators=(",", ":"))

print(f"{len(completed)} of {len(tasks)} tasks are done")