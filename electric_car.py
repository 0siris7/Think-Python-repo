class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f'{self.make} {self.model} {self.year}'
        #self.cookie = 'cookie' #Createing attributes outside __init__ is considered bad
        #print(self.cookie)
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, mileage):
        self.odometer += mileage

    def fill_gas_tank(self):
        print('I\'ve filled the gas tank')


class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery")

    def get_range(self):
        
        if self.battery_size == 70:
            range = 240

        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {range}'
        message += ' miles on full charge.'
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    '''def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery.")'''

    def fill_gas_tank(self): #overriding a parent method
        print("Electric cars dont have gas tanks")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
#my_tesla.fill_gas_tank()
