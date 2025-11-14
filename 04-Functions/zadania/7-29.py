def factorial(n):
    numbers = []
    for num in range(n+1):
        if num==0 or num==1:
            numbers.append(1)
        elif num>1:
            temp = 1
            for x in range(1, num+1):
                temp *= x
            numbers.append(temp)

    return numbers[-1]
print(factorial(5))


