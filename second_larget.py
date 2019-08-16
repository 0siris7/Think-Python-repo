numbers = [int(x) for x in input().split()]
print(numbers)
numbers.sort(reverse = True)
print(numbers[1], numbers[len(numbers) - 2])
