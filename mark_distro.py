n, m = [int(x) for x in input().split()] #n number of elements ; m number of students
a = [int(x) for x in input().split()] #list of marks
a.sort()
b = a[:m]

print(b[m - 1] - b[0])