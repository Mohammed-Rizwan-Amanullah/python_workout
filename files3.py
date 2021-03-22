user_name = input("enter the name of the user: ")

file_name = 'user_details.txt'

with open(file_name, 'w') as file_object:
    file_object.write(f"The name of the user is {user_name}, \n ")
    action = True;
    while action:
        user_name = input("enter the name of another user: ")
        print(f"welcome, {user_name.title()}")
        file_object.write(f"The name of the visitor is {user_name} \n")
        print("Recorded your visit details in visiting document\n")
        additional_person = input("Is there anyone else with you? y/n")
        if additional_person == 'y':
            continue;
        else:
            action = False
            break

with open(file_name, 'a') as file_object:
    action = True;
    while action:
        reason = input("why do you like programming?")
        file_object.write(f"the user likes programmming because {reason} \n")
        print("thank you for your response, your details has been recorded")
        additional_person = input("is there is anyone else with you? y/n")
        if additional_person == 'y':
            continue
        else:
            action = False;
            break
