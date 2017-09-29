import requests

url = input('Site address: ')
response = requests.get(url).text

print(response)
