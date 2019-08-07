try:
    with open('cat.txt') as c1:
        cats = c1.read()



except:
    pass

else:
    print(cats)


try:

    with open('god.txt') as d1:
        dogs = d1.read()

except:
    pass

else:
    print(dogs)
