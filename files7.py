#dumping number to json file
import json

user_fav_number = input("Enter your fav number")

file_name = 'fav_number.json'

with open(file_name, 'w') as f:
    json.dump(user_fav_number, f)

print("user favourite number stored in json file")

