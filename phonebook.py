import sys
phoneBook = {}
for _ in range(int(input())):
    name, phone = input().split()
    phoneBook[name] = phone

queries = sys.stdin.readlines()

for query in queries:
    if query in phoneBook:
        print(f"{query}={phoneBook[query]}")
    
    else:
        print("Not found")