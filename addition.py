try:
    inp = 'y'
    sum = 0
    while inp != 'q':
        inp = input('Wish to continue?')
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        ssum = a + b


except ValueError:
    pass

else:
    print(ssum)
