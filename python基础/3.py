import string
import requests

name = "zhao bi cheng"
print(name.find("bi"))

print(name.upper())

print(name.replace("bi", "ci"))

r = requests.get(r"https://api.github.com/users/acombs/starred")
r.json()
print(r.json())
