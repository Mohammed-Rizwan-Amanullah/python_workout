items = ["apple","mango","orange","guava","lemon","grapes"]
print(f"the first three items in the list are {items[0:3]}")

for item in items[0:3]:
    print(item)

print("various combination of slices")
print(items)
for item in items[2:]:
    print(item)
print("this is the slice of[2:0]starting from second element till last element\n")

for item in items[:3]:
    print(item)
print("this is the slice of[:3]starting from fist element till third element\n")

for item in items[-3:]:
    print(item)
print("this is the slice of[-3:0]printing the last three element\n")

for item in items[:-3]:
    print(item)
print("this is the slice of[:-3]printing from first element leaving last three element\n")


print("\nnext exercise")
movies = ["batman","batman begins","batman dark knight","batman dark knight rises","lord of the rings 1","lord of the rings 2"]
cinemas = movies[:]
print(movies)
print(cinemas)
cinemas.append("lotr3")
movies.append("spiderman")
print(movies)
print(cinemas)

print("\n using for loop to print movies in movie list")
for movie in movies:
    print (movie)

print("\n using for loop to print cinema in cinema list")
for cinema in cinemas:
    print(cinema)
