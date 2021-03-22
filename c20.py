responses = {}
polling_status = True

while polling_status:
    name = input("what is your name? ")
    response = input("where would you like to go? ")
    responses[name] = response
    nex = input("anyone else is there yes/no? ")

    if nex == "no":
        polling_status = False

print("\nLet's see the result of the poll")
for key, value in responses.items():
    print(f"{key.title()} likes to go to {value.title()}")

