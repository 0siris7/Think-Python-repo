filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("ENTER YOUR NAME:\n"))


with open(filename, 'a') as file_object:
    while True:
        name = input("Enter name:")
        if name == 'q' or name == 'quit':
            print("QUIT")
            break

        else:
            print("Hello {}".format(name))
            file_object.write(f"{name} entered as guest\n")
