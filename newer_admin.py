from new_user import User

class Admin(User):
    def __init__(self, first_name, last_name,password, age, privi):
        super().__init__(first_name, last_name, password, age)
        self.privileges = privi

    def show_privileges(self):
        for i in self.privileges:
            print(i, end = ' ')

        print('\n')
