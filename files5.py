file_name = 'cats.txt'
try:
    with open(file_name) as f:
        cats_name = f.readlines()
except FileNotFoundError:
    print("cats.txt file is not present.Please check the file location and try again")
else:
    print("these are the cats present in that file")
    for cat in cats_name:
        print(cat.rstrip())

file_name = 'dogs.txt'
try:
    with open(file_name) as f:
        dogs_name = f.readlines()
except FileNotFoundError:
    pass
    print("dogs.txt file is not present.Please check the file location and try again")
else:
    print("\nthese are the dogs present in that file")
    for dog in dogs_name:
        print(dog.rstrip())
