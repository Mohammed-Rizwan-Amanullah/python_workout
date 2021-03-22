#exercise 1
class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        print(f"the name of the restaurant is {self.restaurant_name.upper()}")
        print(f"our special cuzine is {self.cusine_type.title()}")
        print(f"the number of customer served is {self.numbers_served}")

    def open_restaurant(self):
        print("our restaurant is open")

    def set_numbers_served(self, new_number):
        self.numbers_served = new_number
        print(self.numbers_served)

    def increment_numbers_served(self, increment_value):
        self.numbers_served += increment_value


my_restaurant = Restaurant("eternal cusines", "sounth indian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_numbers_served(15)
my_restaurant.increment_numbers_served(100)
print(my_restaurant.numbers_served)
