import random
matrix = [[random.randint(1,9) for x in range(5)] for x in range(3)]

for row in matrix:
    print(row)

matrix[0], matrix[-1] = matrix[-1], matrix [0]

print("zamiana row 0 z row 2")
for row in matrix:
    print(row)


print("zamiana kolumny 0 z kolumna 2")
for row in matrix:
    row[0], row[-1] = row[-1], row[0]


for row in matrix:
    print(row)