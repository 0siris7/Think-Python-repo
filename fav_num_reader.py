import json

filename = 'fav.json'
num = input("Enter your favorite number: ")
try:
    with open(filename, 'w') as fobj:
        json.dump(num, fobj)

except FileNotFoundError:
    pass
