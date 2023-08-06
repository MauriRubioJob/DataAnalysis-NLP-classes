import math
import random

xs = lambda min, max, n: [(max - min) / n * i for i in range(n)]
sin = lambda xs: [math.sin(x) for x in xs]
cos = lambda xs: [math.cos(x) for x in xs]
zero_to_one_random = lambda xs: [random.random() for _ in xs]
ascending = lambda xs: [(random.random() * 0.4 - 0.2) + x / len(xs) for x in xs]


from matplotlib import pyplot


# Line plot
# pyplot.plot(x_coords, y_coords)

# Scatter plot
# pyplot.scatter(x_coords, y_coords)

# Scatter plot
# pyplot.bar(x_coords, y_coords)
# pyplot.show()


x_coords = xs(0, math.pi * 2, 100)
y_coords_1 = sin(x_coords)
y_coords_2 = zero_to_one_random(x_coords)


figure, axes = pyplot.subplots(nrows=2, ncols=1)
figure.suptitle("Multiple plots")

axes[0].plot(x_coords, y_coords_1, linestyle="dashed")
figure.set_label("Y coords")
axes[1].scatter(x_coords, y_coords_2, marker=".", color="r")

pyplot.show()
