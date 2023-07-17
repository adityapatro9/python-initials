import requests

r = requests.get('http://localhost:8080/about')
print(r)
print(r.content)

