#exercise 1
class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(f"the name of the restaurant is {self.restaurant_name.upper()}")
        print(f"our special cuzine is {self.cusine_type.title()}")

    def open_restaurant(self):
        print("our restaurant is open")


my_restaurant = Restaurant("eternal cusines", "sounth indian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#exercise 2
class User:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def describe_user(self):
        print(f"the name of the user is {self.first_name} {self.last_name}")
        print(f"age of the user is {self.age}")
        print(f"nationality of the user is {self.nationality}\n")

user_1 = User("Mohammed", "Rizwan", 27, "Indian")
user_1.describe_user()
user_2 = User("Jessica", "Miller", 35, "American")
user_2.describe_user()
user_3 = User("David", "Miller", 45, "American")
user_2.describe_user()
