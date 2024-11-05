class User:
    def __init__(self, first_name, last_name, age, month_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.month_of_birth = month_of_birth

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and was born in {self.month_of_birth}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}. Good to see you.")

user1 = User("John", "Wall", 34, "September")
user2 = User("Kyrie", "Irving", 32, "March")
user3 = User("Reed", "Sheppard", 20, "June")

for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()
