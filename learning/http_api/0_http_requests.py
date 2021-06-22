import requests

url = "https://www.google.com/"
response = requests.get(url)

# print(response)
# print(response.ok)
# print(response.headers)
# print(response.text)

# open .py with terminal
print(f'Request to {url}. Status code is {response.status_code}')
