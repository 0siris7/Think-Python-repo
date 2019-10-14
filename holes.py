one_hole = ['A', 'D', 'O', 'P', 'Q','R']
two_hole = ['B']

string = list(input())
count = 0

for letter in string:   
    if letter in one_hole:
        count += 1

    elif letter in two_hole:
        count += 2

print(count)