import matplotlib.pyplot as plt

x = []
y = []

for n in range(-100,101):
   x.append(n)

# create y values
for n in x:
   y.append(pow(n,2))

# print chart
plt.plot(x, y)
plt.show()
