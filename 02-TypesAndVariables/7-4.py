import math
circumference = float(input("Podaj obwód drzewa: "))
diameter = circumference/math.pi
if diameter >= 50:
    print("Można ściąć")
else:
    print("Nie można ściąć")