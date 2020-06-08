board = [" " for _ in range(9)]
def create_board(board):
    row1 = "\t|{0}|{1}|{2}|".format(board[0], board[1], board[2])
    row2 = "\t|{0}|{1}|{2}|".format(board[3], board[4], board[5])
    row3 = "\t|{0}|{1}|{2}|".format(board[6], board[7], board[8])
    board = " \n{}\t\t\t|1|2|3|\n\t-------\t\t\t-------\n{}\t\t\t|4|5|6|\n\t-------\t\t\t--------\n{}\t\t\t|7|8|9|".format(row1, row2, row3)
    return board

def update_board(bd,p,s):
    if p<=0 or p>9:
        x="loop"
        return x
    elif bd[p-1]==" " and s=="X":
        bd[p-1]="X"
    elif bd[p-1] == " " and s=="O":
        bd[p-1] = "O"
    else:
        x="loop"
        return x
    return print(create_board(bd))

def win_check(bd,i):
    #row checking
    if ((bd[0] == i and bd[1] == i and bd[2] == i) or \
        (bd[3] == i and bd[4] == i and bd[5] == i) or \
            (bd[6] == i and bd[7] == i and bd[8] == i) or \
                (bd[0] == i and bd[3] == i and bd[6] == i) or \
                    (bd[1] == i and bd[4] == i and bd[7] == i) or \
                        (bd[2] == i and bd[5] == i and bd[8] == i) or \
                            (bd[0] == i and bd[4] == i and bd[8] == i) or \
                                (bd[2] == i and bd[4] == i and bd[6] == i)):
                                return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True

def player_move(sign):
    if sign=="X":
        ip=int(input("Enter the number for insertion (X) :").rstrip())   
    else:
        ip=int(input("Enter the number for insertion (O) :").rstrip())
    
    return ip

def main():
    p1 = "'X'"
    p2 = "'O'"
    print('{} - (X)  {} - (O)'.format(p1, p2))
    print(create_board(board))
    while True:
        ip1=player_move("X")
        while update_board(board,ip1,"X")=="loop":
            print("Enter a Valid position!!")
            ip1 = player_move("X")
        else:
            update_board(board, ip1, "X")
        if win_check(board,"X"): 
            print(p1," Wins !!!!")
            break
        if is_draw():
            print("its a Draw!!")
            break
        ip2=player_move("O")
        while update_board(board,ip2,"O")=="loop":
            print("Enter a Valid position!!")
            ip2 = player_move("O")
        else:
            update_board(board, ip2, "O")
        if win_check(board,"O"):
            print(p2, " Wins !!!!")
            break
main()
