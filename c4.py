travel = ["italy","germany","indonesia","newzeland"]
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel,reverse= True))

print("\n testing reverse method")
print(travel.reverse())
print("\n back to original form")
print(travel.reverse())

print("\ntesting sort method")
print(travel.sort())
print(travel.sort(reverse=True))

print("\n no of destinations in the list")
num = len(travel)
print (num)


