matrix = [
    [-38, 19],
    [  5, 40],
    [ -7, 11],
    [ 29, 16]
]

for row in matrix:
    print(max(row), " ", matrix.index(row)+1, row.index(max(row))+1)

