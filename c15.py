favourite_places = {
    'jan' : ['vietnam','laos','cambodia'],
    'hermonie' : ['hongkong','macau','nepal'],
    'rizwan' :['australia','luang prabung','malasia'],
}

for key, value in favourite_places.items():
    print(f"{key} loves the below places")
    for place in value:
        print(place)
    print("\n")
