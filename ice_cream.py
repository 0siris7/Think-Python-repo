class Restaurant():

    def __init__(self, res_name, cusine_name, number_served = 0):
        self.res_name = res_name
        self.cusine_name = cusine_name
        self.number_served = number_served


    def describe_restaurant(self):
        print("{} has {} and has servered {} customers".format(self.res_name,
        self.cusine_name, self.number_served))


    def open_restaurant(self):
        self.open = 'open'
        print(Restaurant.condition)

    def set_number_served(self, number):
        self.number_served =  number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, res_name, cusine_name):
        super().__init__(res_name, cusine_name)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        print("The flavors are:")
        for i in self.flavors:
            print(i,end = ' ')
        print('\n')


ice_cream = IceCreamStand("Le Divine",'Cookie')

ice_cream.display_flavors()
