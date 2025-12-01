import numpy as np
import matplotlib.pyplot as plt

width, height = 1000, 1000
max_iter = 100

# zakres osi
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# tworzymy siatkę kompleksową
xs = np.linspace(xmin, xmax, width)
ys = np.linspace(ymin, ymax, height)
mandelbrot = np.zeros((height, width))

for i, y in enumerate(ys):
    for j, x in enumerate(xs):
        c = complex(x, y)
        z = 0
        it = 0
        while abs(z) <= 2 and it < max_iter:
            z = z*z + c
            it += 1
        mandelbrot[i, j] = it

plt.imshow(mandelbrot, extent=(xmin, xmax, ymin, ymax))
plt.axis("off")
plt.show()
