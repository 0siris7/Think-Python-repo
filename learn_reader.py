with open('learning_python.txt') as fin:
    line = fin.read()

print("NORMAL PRINT")
line = line.replace("Python", 'Ruby')
print(line)

print("LOOP")
with open('learning_python.txt') as fin:
    for line in fin:
        line = line.replace('Python', 'C')
        print(line)


with open('learning_python.txt') as fin:
    line2 = fin.readlines()


line3 = ''

print("LIST")
for li in line2:
    line3 += li.strip()

line3 = [x.replace('Python', 'c++') for x in line3]
print(''.join(line3))
