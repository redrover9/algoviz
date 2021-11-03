import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

keys = []
values = []
for i in range(1, 101):
    keys.append(i)
    values.append(i)
random.shuffle(values)
coordinates_dict = dict(zip(keys, values))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(1, 1, 1)

def algo(i):
    ax.clear()
    length = len(coordinates_dict)
    for i in range(length):
        for j in range(1, length -i):
            if coordinates_dict[j] > coordinates_dict[j + 1]:
                coordinates_dict[j], coordinates_dict[j + 1] = coordinates_dict[j + 1], coordinates_dict[j]
        x_coordinates = []
        y_coordinates = []
        for x in coordinates_dict.keys():
            x_coordinates.append(x)
        for y in coordinates_dict.values():
            y_coordinates.append(y)
        line, = ax.plot(x_coordinates, y_coordinates, color="blue")
        return line,

ani = animation.FuncAnimation(fig, algo)
plt.show()
