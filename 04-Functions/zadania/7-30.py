sum = 0
def sum_natural(n):
    global sum
    sum += n
    if n>0:
        sum_natural(n-1)
    print(sum)
sum_natural(10)