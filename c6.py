#printing the cube value of numbers from 1 to 10
cubes = []
for value in range(1,10):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

#more presice way of writing this program will be

cubes = []
for value in range(1,10):
    cubes.append(value**3)
print(cubes)

#even precise way will be using list comprehension method

list_comprehension = [value**3 for value in range(1,20)]
print(list_comprehension)

#making a list of million and calculating the min max and sum of it
million = []
for value in range(1,1000000):
    million.append(value)
print(min(million))
print(max(million))
print(sum(million))

#list of odd numbers
odd = []
for value in range(1,20,2):
    odd.append(value)
print(cubes)

#multiples of 3
multiples = []
for value in range(1,11):
    multiples.append(value*3)
print(multiples)

