import requests

url = "https://www.google.com/"
response = requests.get(url)

print(response)
print(response.ok)
# print(response.headers)
# print(response.text)

# http responses
# Code. Meaning. Examples:
# 1xx. Information. 100 = serever agrees to handle client`s request
# 2xx. Succes. 200 = request suceeded, 204 = no content present
# 3xx. Redirectoin. 301 = page moved, 304 = cached page still valid
# 4xx. Client error. 403 = forbidden page, 404 = page not found
# 5xx. Server error. 500 = internal server error, 503 = try again later

print(f'Request to {url}. Status code is {response.status_code}')
