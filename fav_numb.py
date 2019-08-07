import json

filename = 'fav.json'

try:
    with open(filename) as fobj:
        numb = json.load(fobj)

except FileNotFoundError:
    numb = input("What's your favorite number?\n>")
    with open(filename, 'w') as fobj:
        json.dump(numb,fobj)

else:
    print(f"Your favorite number is {numb}")
