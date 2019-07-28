def finder(s):
    count = 0
    for i in s:
        if i == 'a' or i == 'A':
            count+= 1
    return count


sample = finder(input("Type yo string"))

print(f"Count: {sample}")
