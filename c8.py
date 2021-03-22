car = "audi"

if car == "Audi":
    print("That is such a superb car")
else:
    print("not a superb car")

#making use of lower method to convert the variable case
if car.lower() == "audi":
    print(f"{car.title()} that is such a superb car")
else:
    print("not a superb car")

#testing the not equal operator
if car != "BMW":
    print("you are not having a car that is BMW")
else:
    print("it is BMW")

#testing if else statement and checking whether the value is in the list or not
planes = ["airbus","indigo","joomla","pacific","power"]
plane = "power"
if plane in planes:
    print(f"{plane.title()} it is there in the plane list")
else:
    print("nope we dont have it in our list")


#testing whether the value in the list or not
plane = "airbnb"

if plane not in planes:
    print("sorry it is not in the list")
else:
    print("congrats it is in the lsit")
