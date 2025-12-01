import os


tic_tac_toe_test = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
win_condition = False
moves = 0

def insert(row, column, sign):
    tic_tac_toe_test[row][column] = sign

def check_win_condition(player):
    # sprawdzanie rzędów
    for row in tic_tac_toe_test:
        if row[0] == row[1] and row[1] == row[2] and row != ["-","-","-"]:
            print(f"Wygrywa {player}")
            return True
            
    # sprawdzanie kolumn
    columns = [[],[],[]]
    for row in tic_tac_toe_test:
        a=0
        for ele in row:
            columns[a].append(ele)
            a+=1
    for column in columns:
        if column[0] == column[1] and column [1] == column[2] and column != ["-","-","-"]:
            print(f"Wygrywa {player}")
            return True
        
    # sprawdzanie ukosów
    if tic_tac_toe_test[0][0] == tic_tac_toe_test[1][1] and tic_tac_toe_test[2][2] == tic_tac_toe_test[1][1] and tic_tac_toe_test[1][1] != "-":
        print(f"Wygrywa {player}")
        return True
    if tic_tac_toe_test[0][2] == tic_tac_toe_test[1][1] and tic_tac_toe_test[1][1] == tic_tac_toe_test[2][0] and tic_tac_toe_test[1][1] != "-":
        print(f"Wygrywa {player}")
        return True
    
    # czy remis
    if moves == 9:
        print("Remis")
        return True

    return False

def print_board():
    os.system('cls')
    for x in tic_tac_toe_test:
        print(x)

def main():
    global moves
    global win_condition
    player = False
    gracz = ""
    znak = ""
    print_board()

    while win_condition == False:
        moves += 1
        player = not player
        if player:
            gracz = "Gracz 1"
            znak = "X"
        if not player:
            gracz = "Gracz 2"
            znak = "O"

        move_input = input(f"{gracz} wykonaj ruch: ").split(",")
        while int(move_input[0]) not in range(0,3) or int(move_input[1]) not in range(0,3):
            print_board()
            print("Zła notacja")
            move_input = input(f"{gracz} wykonaj ruch: ").split(",")    

        while tic_tac_toe_test[int(move_input[0])][int(move_input[1])] in ("X", "O"): # sprawdza czy nie bylo juz ruchu w tym miejscu
            print_board()
            print("Ruch został już wykonany w tym miejscu")
            move_input = input("Gracz 1 wykonaj ruch: ").split(",")

        insert(int(move_input[0]),int(move_input[1]), znak)
        print_board()
        win_condition = check_win_condition(gracz)
if __name__ == "__main__":
    main()
