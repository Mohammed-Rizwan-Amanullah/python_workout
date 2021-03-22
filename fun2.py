#exercise1
def make_shirt(sizeof, mesageof):
    print(f"the size of the shirt is {sizeof}")
    print(f"the message that will be printed in the shirt is '{mesageof}'\n")

make_shirt(sizeof = 45, mesageof = "the world is your limit") #keyword arguments
make_shirt(55,"denim")#position arguments

#exercise 2

def make_shirt(sizeof = "large", mesageof = "i love python"):
    print(f"the size of the shirt is {sizeof}")
    print(f"the message to be printed in the shirt is '{mesageof}'\n")

make_shirt()
make_shirt("medium")
make_shirt("small", "take your time")

#exercise 3

def describe_city(city, country = 'india'):
    print(f"the city {city} is in country {country} \n")

describe_city("chennai")
describe_city("mumbai")
describe_city("sydney", "australia")
