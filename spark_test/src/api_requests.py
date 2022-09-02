import requests

response = requests.get("https://jsonplaceholder.typicode.com/")
print(response.status_code)
print(response)

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response)
