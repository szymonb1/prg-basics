import matplotlib.pyplot as plt
import math


x_points = [x for x in range(361)]
y_points = [math.sin(math.radians(x)) for x in x_points]

plt.plot(x_points, y_points)
plt.show()
