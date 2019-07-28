from math import sqrt


def mysqrt(a):
    x = 3
    y = (x + (a/x)) / 2
    while True:
        if abs(y - x) < 0.0000001:
            return y
        else:
            x = y
            y = (x + (a/x)) / 2



def test_square_root():
    a = int(input("Enter the number (a): >"))
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff".center(30))
    for i in range(1, a + 1):
        #i = float(i)
        print(f"{i}\t{mysqrt(i)}\t{sqrt(i)}\t{abs(mysqrt(i) - sqrt(i))}".center(30))

test_square_root()
