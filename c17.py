#odd or even no
number = input("enter the number")
number = int(number)

if number % 2 == 0:
    print("the number is a even no")
else:
    print("the no is odd")

#exercise
car = input("enter the car which you want to rent")
print(f"let me see if i can find {car.title()} in our garage")

#exercise 2

dinners = input("enter the number of people ")
dinners = int(dinners)
if dinners > 8:
    print("the no of people is more so wait for 30 minutes")
else:
    print("we have assigned table no 4 for you. enjoy our food")

#exercise 3

number = input("enter the number")
number = int(number)
if number % 10 == 0:
    print("the number is divisible by 10")
else:
    print("the number is not divisible by 10")

