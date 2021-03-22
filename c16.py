cities = {
    'bangalore' : {
    'state' : 'karnataka',
    'country' : 'india',
    'type' : 'metro'},

    'mumbai' : {
    'state' : 'maharastra',
    'country' : 'india',
    'type' : 'metro'
    },

    'hyderabad' : {
    'state' : 'AP',
    'country' : 'india',
    'type' : 'metro'
    },
}

for city, info in cities.items():
    print(f"\n{city} has following information")
    for detail, stat in info.items():
        print(f"{detail} {stat}")
