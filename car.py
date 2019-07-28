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
            self.odometer += mileage
        else:
            print("You can't roll back an odometer")

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
