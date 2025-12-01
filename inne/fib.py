def f(number):
    fib_prev = 0
    fib = 0
    while number >= fib:
        if (number == fib):
            return True
        
        if (fib == 0):
            fib = 1
        else:
            temp = fib
            fib += fib_prev
            fib_prev = temp

    return False