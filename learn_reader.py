with open('learning_python.txt') as fin:
    line = fin.read()

print("NORMAL PRINT")
print(line)


print("LOOP")
with open('learning_python.txt') as fin:
    for line in fin:
        print(line)


with open('learning_python.txt') as fin:
    line2 = fin.readlines()


line3 = ''

print("LIST")
for li in line2:
    line3 += li.strip()

print(line3)
