import requests
url = "http://127.0.0.1:5000/api/joke"
response = requests.get(url)
print(response.json())


"""
url = "http://127.0.0.1:5000/api/jokes/2"
response = requests.get(url)
print(response.json())
"""
# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke

