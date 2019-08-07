import json
filename = 'fav.json'

try:
    with open(filename) as fobj:
        numb = json.load(fobj)

except FileNotFoundError:
    pass

else:
    print(f"I know your favorite number, its {numb}")
