destination = int(input())
x = 0
jump = 0
jumps = []

for i in range(destination):
    if jump == 0:
        x += 1
        jumps.append(x)
        jump += 1

    if jump == 1:
        x += 2
        jumps.append(x)
        jump += 1
    
    if jump == 2:
        x += 3
        jumps.append(x)
        jump = 0

if destination in jumps:
    print("YES")

else:
    print("NO")