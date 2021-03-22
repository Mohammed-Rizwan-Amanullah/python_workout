#checkin if json file is present. if not, creating new json file
import json

file_name = 'fav_number.json'
try:
    with open(file_name) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    user_fav_number = input("Enter your fav number")
    with open(file_name, 'w') as f:
        json.dump(user_fav_number, f)
    print("We will remember your favourite number\n")
else:
    print(f"the fav number that user wrote was {fav_num}")


