from requests import get
from sys import argv

print(get(argv[1]).text)
