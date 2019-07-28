def recur(n):
    if n == 1:
        return n
    else:
        return n * recur(n - 1)

tot = 1
print(recur(5))
