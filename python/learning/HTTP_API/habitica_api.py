import requests
import myinfo

json_payload = {
    "text": "Test Task 2",
    "type": "todo",
    "alias": "hab-api-tasks",
    "notes": "This is a test task that was set with the python requests module.",
    "priority": 2,
}
headers = {
    "Content-Type": "application/json",
    "x-api-user": myinfo.habitica_api_user,
    "x-api-key": myinfo.habitica_api_key,
    "x-client": myinfo.habitica_api_key + "-Testing"
}
response = requests.post("https://habitica.com/api/v3/tasks/user", json=json_payload, headers=headers)
print(response)

data = response.json()
for value in data.items():
    print(value)
