class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f'{self.make} {self.model} {self.year}'
        #self.cookie = 'cookie'
        #print(self.cookie)
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#print(my_new_car.cookie)
