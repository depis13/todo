import requests

headers = {
    'Origin': 'http://localhost:3000',
    'Access-Control-Request-Method': 'GET',
}

response = requests.options('http://127.0.0.1:8000/api/v1/users', headers=headers)
print(response.status_code)
print(response.text)