import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors=None, s=10)
    ax.scatter(0,0, c='green', edgecolors=None, s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolors=None, s=50)
    plt.show()

    keep = input("Do you want to generate another walk? (Y/N)")
    if keep == "n":
        break
