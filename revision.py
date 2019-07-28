'''A script to practice all that was learned

"""Lists"""
a = list()
b = [12]
for i in range(10): #If trying to a append a list the whole list along with the brackets are appended
    a.append(i)

b.extend(a)
print(a, b)


c = [x  if x % 2 == 0 else x + 1 for x in range(len(b))] #List comprehension

print(c)
#More list comprehension
sample = [str(x) if x % 2 == 0 else '4k' for x in range(len('hello'))]
print('-'.join(sample))'''
