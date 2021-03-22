unverified_users = ['jack','john','mick','mickey']
verified_users = []

print("the unverified user in the list are")
for unverified in unverified_users:
    print(unverified)

while unverified_users:
    current_user = unverified_users.pop()
    print(f"\nI'm verifying {current_user} now")
    print("the user is verified")
    verified_users.append(current_user)

print("below users are verified")
for verified in verified_users:
    print(verified)

unverified_user_number = len(unverified_users)
print("current unverified user is " + str(len(unverified_users)))
