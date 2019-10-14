numbers = [x for x in input().split()]

count = 0

for i in numbers:
    if i == '0':
        count += 1
        del numbers[numbers.index(i)]

for _ in range(count):
    numbers.append('0')

print(' '.join(numbers))