print("enter the number of person")
number = input()
number = int(number)
n = 0
while n < number:
    age = input("enter the age of the member to know the price")
    n += 1
    age = int(age)
    if age <= 3:
        print("the ticket is free for this person")
    elif age <= 12:
        print("the ticket is $10 for this person")
    elif age > 12:
        print("the ticket is $15 for this person")

