matrix = [

]
def fmatrix(n):
    for row in range(n):
        matrix.append([0]*n)
    i = 0
    for row in matrix:
        row[i] = 1
        i+=1

    for row in matrix:
        print(row)

fmatrix(6)