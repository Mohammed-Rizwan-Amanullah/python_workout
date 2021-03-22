#reading favourite number from json file

import json

file_name = 'fav_number.json'

with open(file_name) as f:
    fav_num = json.load(f)

print(f"the fav number that user wrote was {fav_num}")
