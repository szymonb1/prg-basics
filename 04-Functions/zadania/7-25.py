def f(x,y):
    sum = 0
    for n in range(x,y+1):
        if n%2 == 0 and n%3 == 0 and n%4 != 0:
            sum += n
        else:
            pass

    print(sum)
f(10, 30)