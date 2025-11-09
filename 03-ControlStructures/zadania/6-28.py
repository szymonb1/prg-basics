def Fib(x):
    if x<0:
        print("incorrect")
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return Fib(x-1) + Fib(x-2)



amount = int(input("Podaj ile liczb fibonacciego: "))
for x in range(amount):
    print(Fib(x), end=' ')
