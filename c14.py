person_1 = {'first_name' : 'mohammed',
            'second_name' : 'rizwan',
            'city' : 'thanjavur',
            'state' : 'tamil nadu',
            }
person_2 = {'first_name' : 'nandha',
            'second_name' : 'kumaran',
            'city' : 'thanjavur',
            'state' : 'tamil nadu',
            }
person_3 = {'first_name' : 'suchi',
            'second_name' : 'suchi',
            'city' : 'bangalore',
            'state' : 'karnataka',
            }
persons = [person_1, person_2, person_3]

for person in persons:
    for key, value in person.items():
        print(f"{key} is " + f"{value}")
    print("\nnext person")
