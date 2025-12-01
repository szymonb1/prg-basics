matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposed_matrix = []

def transpose(matrix):
    for row in matrix:
        transposed_matrix.append([0]*len(row))

    i = 0
    for row in matrix:
        j = 0
        for x in row:
            transposed_matrix[j][i] = x
            j+=1        
        i+=1

    for row in matrix:
        print(row)
    print("--------")
    for row in transposed_matrix:
        print(row)
       
transpose(matrix1)
