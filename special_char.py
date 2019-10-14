import re

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

string = input()

if regex.search(string) == None:
    print("NO")

else:
    print("YES")