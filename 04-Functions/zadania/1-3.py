import math as m

def triangle_area(a,b,c):
    s = (a+b+c)/2
    result = m.sqrt(s*(s-a)*(s-b)*(s-c))
    return result

a=7
b=24
c=25

print(f'The area of ​​a triangle with sides {a,b,c} is {triangle_area(a,b,c)}')
