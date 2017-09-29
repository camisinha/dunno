from requests import get

url = input('Site address: ')
response = get(url).text

print(response)
