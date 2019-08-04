filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming\n')
    file_object.write("I love creating games \n")

with open(filename, 'a') as file_object:
    file_object.write('I love cookies too.\n')
    file_object.write('and naruto.\n')
