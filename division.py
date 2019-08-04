print("Give me two numbers, I'll divide them")
print("Enter 'q' to exit")

while True:
    first_number = input("FIRST NUMBER")
    if first_number == 'q':
        break

    second_number = input("SECOND NUMBER:")

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("No zero allowed")

    else:
        print(answer)
