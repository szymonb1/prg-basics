
def prime_number(n):
    if n<1:
        return "zle"
    elif n == 1:
        return "zle"
    elif n == 2 or n==3:
        return n
    else:
        for x in range(2, n):
            if n%x == 0:
                return
            else:
                continue
        else:
            return n
for x in range(2,200000):
    if prime_number(x) != None:
        print(prime_number(x), end=' ')
    else:
        pass
