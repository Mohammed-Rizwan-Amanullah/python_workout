#when there is user in the list

users = ["jack","john","martha","jones","admin"]

for user in users:
    if user == "admin":
         print("welcome macha you have to do the work now")
    else:
        print(f"welcome {user}")

print("\n enjoy the user experience")


#if ther is no user in the list
users = ["jack","john","martha","jones","admin"]

print("\n testing when there is no user in the list")
if users:
    for user in users:
        if user == "admin":
            print("welcome macha you have to do the work now")
        else:
            print(f"welcome {user}")
else:
    print("unfortunately there are no users in the list")

print("\n enjoy the user experience")


#testing all user has unique name
print("TEsting the user has unique name")
current_users = ["jack","john","martha","jones","admin"]
new_users = ["ryan","pam","martha","jones","joey"]

for new_user in new_users:
    if new_user in current_users:
        print(f"Hey your user name {new_user} is already in our list so try something new")
    else:
        print(f"your user name is not in the list {new_user}")


#testing the if elif and else

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(f"the number is {number}st")
    elif number == 2:
        print(f"the number is {number}nd")
    elif number == 3:
        print(f"the number is {number}rd")
    elif number > 3:
        print(f"the number is {number}th")
