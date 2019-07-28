class User():
    def __init__(self, first_name, last_name, password, age):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.login_attempt = 0

    def describe_user(self):
        print("Name: {} {}\nAge: {}\nPassword: {}".format(self.first_name,
        self.last_name, self.age, self.password))

    def greet_user(self):
        print("Greetings {} {}".format(self.first_name,self.last_name))

    def increment_login_attempt(self):
        self.login_attempt += 1
        print(self.login_attempt)
        if self.login_attempt > 3:
            print("NO MORE ATTEMPTS")

    def reset_login_attempt(self):
        self.login_attempt = 0


gary = User('Gary', 'Oldman', 'asphixsia', 56)
gary.describe_user()
gary.greet_user()

gary.increment_login_attempt()
gary.increment_login_attempt()
gary.increment_login_attempt()
gary.increment_login_attempt()
gary.reset_login_attempt()

gary.increment_login_attempt()
