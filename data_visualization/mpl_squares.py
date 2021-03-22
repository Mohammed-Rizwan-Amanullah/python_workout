import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
square = [1, 4, 9, 16, 25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

ax.plot(input_values, square, linewidth=3)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()
