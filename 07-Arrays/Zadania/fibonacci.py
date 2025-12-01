def fibonacci(n):
    fibonacci = []
    for x in range(n):
        if x == 0:
            fibonacci.append(0)
        elif x == 1:
            fibonacci.append(1)
        else:
            temp = fibonacci[x-1] + fibonacci[x-2]
            fibonacci.append(temp)
    return fibonacci
print(fibonacci(6))