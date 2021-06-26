# guide: https://python-scripts.com/requests#method-get-requests
import requests
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from getpass import getpass

# Get info from url
response_get = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    timeout=3.05  # or timeout(2, 5)  # until 2 sec - connect user with app, until 5 wait response from server
)

# print(f'response get: {response_get}, status code: {response_get.status_code}, {response_get.ok}')
# response_get.encoding = 'utf-8'  # for .get
# print(response_get.content)  # recieve byte info
# print(response_get.text)  # recieve text info
# print(response_get.headers)  # http headers
# print(response_get.headers['Content-Type'])  # payload type

json_response = response_get.json()
repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')  # Python 3.6+
# print(f'Repository description: {repository["description"]}')  # Python 3.6+
# print(f'Text matches: {repository["text_matches"]}')  # headers allow this
# print(f'License: {repository["license"]}')

response_post = requests.post(
    'https://httpbin.org/post',
    data={'key_meow': 'value_meow'}
)

# print(f'response post: {response_post}, status code: {response_post.status_code}, {response_post.ok}')
# response_post.encoding = 'utf-8'  # for .get
# print(response_post.content)
# print(response_post.text)

requests.post('https://httpbin.org/post', data={'key': 'value'})
# or json={'key':'value'} and json_response = response.json()
requests.put('https://httpbin.org/put', data={'key': 'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key': 'value'})
requests.options('https://httpbin.org/get')


# Authentication
sign_in = requests.get(
    'https://api.github.com/user',
    auth=('name', 'password')
)
print(sign_in)

try:
    response = requests.get('https://api.github.com', timeout=10)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')

# используя менеджер контента, можно убедиться, что ресурсы, применимые
# во время сессии будут свободны после использования
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response_session = session.get('https://api.github.com/user')

print(response_session.headers)
print(response_session.json())


github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# использование `github_adapter` для всех запросов, которые начинаются с указанным URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
