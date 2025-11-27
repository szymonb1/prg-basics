###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math
radius = float(input("Podaj promień koła: "))
pi = math.pi
area = pi * math.pow(radius, 2)
circumference = 2*pi*radius
print(area, circumference)