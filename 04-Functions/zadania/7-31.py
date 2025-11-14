def power(x, n):
    if n==0:
        return 1 
    elif n>0:
        return x*power(x, (n-1))
    else:
        print("error")

print(power(888,221))
