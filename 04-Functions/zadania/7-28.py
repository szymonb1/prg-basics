def f(dice):
    in_row = 0
    number = 0
    for n in range(len(dice)):
        if dice[n] == dice[n-1] and n>0:
            in_row += 1
            number = int(dice[n]) if int(dice[n]) > number else number
        else:
            in_row = 0
            continue
    return number  



print(f("2133888832636262175610274"))