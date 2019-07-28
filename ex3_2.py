def do_twice(f, val):
    f(val)
    f(val)

def print_spam(val):
    print(val)


do_twice(print_spam, input("Enter something: "))
