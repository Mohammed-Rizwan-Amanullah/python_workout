#exercise1
#passing arbitrary values to function and saving the values as tuples
def sandwitches(*toppings):
    for topping in toppings:
        print(f"    - {topping}")

print("The below toppings are added for the order 101")
sandwitches("chicken", "tomatoes", "cheese cubs", "onions")

#exercise 2
#building user profile by storing values into dictinary

def user_profile(first, last, **additional_info):
    additional_info["First name"] = first
    additional_info["Last name"] = last
    return additional_info

user_profile_1 = user_profile("Jack", "Ryan",
                            language = "english",
                            country = "indian",
                            marital_status = "single")

