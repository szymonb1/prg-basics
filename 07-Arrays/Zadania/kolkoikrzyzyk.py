tic_tac_toe_test = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def insert(row, column, sign):
    tic_tac_toe_test[row][column] = sign
insert(1,1,"X")
print(tic_tac_toe_test)
