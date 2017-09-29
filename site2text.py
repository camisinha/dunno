from requests import get
from sys import argv

response = get(argv[1]).text

print(response)
