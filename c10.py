alien_0 = {'color' : 'green', 'points' : 5}

new_points = alien_0['points']
print(f"hey you killed an alien, congrats! take this {alien_0['points']} points")
alien_0["x_axis"] = 5
alien_0['y_axis'] = 10

print(alien_0)

alien_0['x_axis'] = 15

print(alien_0)


#checking out the program given in the book

alien_1 = {'color' : 'green','gender' : 'male', 'x_axis' : 5, 'y_axis' : 10, 'speed' : 'medium'}

print(alien_1)

#incrementing the values based on the speed of the alien

if alien_1['speed'] == 'slow':
    print("your alien is slow")
    x_increment = 5
elif alien_1['speed'] == 'medium':
    print("your alien is medium")
    x_increment = 10
else:
    print("your alien is speed")
    x_increment = 15

print(f"\n\n\nyour alien is {alien_1['speed']}")
alien_1['x_axis'] = alien_1['x_axis'] + x_increment
print(alien_1)
