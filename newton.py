a = int(input("Enter a: \n>"))
x = int(input("Enter x: \n>"))

print(f"Find root of {a} with estination {x}")

y = (x + (a/x)) / 2

print(f"Root: {y}")

while True:
    if abs(y - x) < 0.0000001:
        break
    else:
        x = y
        y = (x + (a/x)) / 2
        print(f"Root: {y}")
