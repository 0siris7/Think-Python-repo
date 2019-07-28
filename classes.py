class Dog():
    '''DOG CLASS'''

    def __init__(self, name, age): #self is a reference to the instance(object)
        '''Initialize attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''simulate sitting'''
        print(f"{self.name.title()} is sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

    def sample(self):
        print('within class')
        self.rover = 'Daisy'
        print(self.rover)

jake = Dog('Jake', 13)
#lucy = Dog('lucy', 15)
jake.sit()
jake.roll_over()

jake.rover = 'lol'

print(jake.rover)

jake.sample()
