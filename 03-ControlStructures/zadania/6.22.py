for x in range(1,31):
    if x%5 == 0 and x%3 == 0:
        print("BINGO", end=" ")
    elif x%5 == 0:
        print("FIVE", end=" ")
    elif x%3 == 0:
        print("THREE", end=" ")
    else:
        print(x, end=" ")