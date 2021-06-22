import requests

json_payload = {
    "text": "Test Task",
    "type": "todo",
    "alias": "hab-api-tasks",
    "notes": "This is a test task that was set with the python requests module.",
    "priority": 2,
}
headers = {
    "Content-Type": "application/json",
    "x-api-key": "9d6fdd4e-9078-4ee5-bdaf-9bb05490418d",
    "x-api-user": "a1ff466f-5563-40f4-b17a-c37bb7b6811b",
    "x-client": "a1ff466f-5563-40f4-b17a-c37bb7b6811b-Testing"
}
response = requests.post("https://habitica.com/api/v3/tasks/user", json=json_payload, headers=headers)
print(response)

data = response.json()
for value in data.items():
    print(value)
