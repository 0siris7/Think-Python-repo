class Restaurant():

    def __init__(self, res_name, cusine_name, number_served = 0):
        self.res_name = res_name
        self.cusine_name = cusine_name
        self.number_served = number_served


    def describe_restaurant(self):
        print("{} has {} and has servered {} customers".format(self.res_name,
        self.cusine_name, self.number_served))


    condition = 'open'
    def open_restaurant(self):
        self.open = 'open'
        #print(f"{self.res_name} is {self.open}")
        print(Restaurant.condition)

    def set_number_served(self, number):
        self.number_served =  number

    def increment_number_served(self, increment):
        self.number_served += increment


def main():
    restaurant = Restaurant('The Restaurant', 'Pizza')
    restaurant.open_restaurant()
    restaurant.describe_restaurant()
    restaurant.set_number_served(50)
    restaurant.describe_restaurant()
    restaurant.increment_number_served(20)
    restaurant.describe_restaurant()


if __name__ == '__main__':
    main()
