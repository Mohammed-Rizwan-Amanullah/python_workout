# ex 1, handlng valueerror exception using try-except-else
print("enter two numbers to add them")
number_1 = input("number 1 ")
number_2 = input("number 2 ")
try:
    sum_of_numbers = int(number_1) + int(number_2)
except ValueError:
    print("You have entered non numeric character")
else:
    print(sum_of_numbers)

print("exercise 2")

 #2 using try-else-error in while loop

while True:
    print("enter two numbers to add them. press 'q' to quit")
    number_1 = input("number 1 ")
    if number_1 == 'q':
        break
    number_2 = input("number 2 ")
    if number_2 == 'q':
        break
    try:
        sum_of_numbers = int(number_1) + int(number_2)
    except ValueError:
        print("something is wrong lets try again")
        pass
    else:
        print(sum_of_numbers)
