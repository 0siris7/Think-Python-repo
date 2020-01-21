import string 

lower = string.ascii_lowercase
upper = string.ascii_uppercase

string = list(input())
i = 0
while i <= len(string) - 1:
    if string[i] == ' ':
        del string[i]
    
    i += 1

count_1 = 0
count_2 = 0

for letter in string:
    if letter in lower:
        count_1 += 1

    elif letter in upper:
        count_2 += 1

tot = str(count_2) + ' ' + str(count_1)

print(tot)
