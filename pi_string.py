filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


pi_string = ''
for line in lines:
    pi_string += line.strip()

#print(pi_string[:52], len(pi_string))

birthday = input("ENTER birthay:")
if birthday in pi_string:
    print("It appears")

else:
    print("It doesnt appear")
