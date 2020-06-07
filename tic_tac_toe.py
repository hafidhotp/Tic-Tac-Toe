
def create_board(board):
    row1 = "\t|{0}|{1}|{2}|".format(board[0], board[1], board[2])
    row2 = "\t|{0}|{1}|{2}|".format(board[3], board[4], board[5])
    row3 = "\t|{0}|{1}|{2}|".format(board[6], board[7], board[8])
    board = " \n{}\t\t\t|1|2|3|\n\t-------\t\t\t-------\n{}\t\t\t|4|5|6|\n\t-------\t\t\t--------\n{}\t\t\t|7|8|9|".format(row1, row2, row3)
    return board



def update_board(bd,p1=" ",p2=" "):
    if bd[p1-1]==" ":
        bd[p1-1]="X"
    elif bd[p2-1]==" ":
        bd[p2-1]="O"
    else:
        pass
    return print(create_board(bd))


def win_check(bd):
    #row checking
    for i in [0,3,6]:
        if ((bd[i] == "X" and bd[i+1] == "X" and bd[i+2] == "X") 
        or (bd[i] == "O" and bd[i+1] == "O" and bd[i+2] == "O")):
            return True

    #diag checking
    for i in [0,2]:
        if ((bd[i] == "X" and bd[i+4] == "X" and bd[i+8] == "X")
                or (bd[i] == "O" and bd[i+4] == "O" and bd[i+8] == "O")):
            return True
        elif ((bd[i] == "X" and bd[i+2] == "X" and bd[i+4] == "X")
                or (bd[i] == "O" and bd[i+2] == "O" and bd[i+4] == "O")):
            return True

    #col checking
    for i in [0,1,2]:
        if ((bd[i] == "X" and bd[i+3] == "X" and bd[i+6] == "X")
                or (bd[i] == "O" and bd[i+3] == "O" and bd[i+6] == "O")):
            return True

board = [" " for _ in range(9)]

def main():
    p1 = 'player 1'
    p2 = 'player 2'
    print('{} - (X)  {} - (O)'.format(p1, p2))
    print(create_board(board))
    gameover=False
    while not gameover:
        ip1,ip2=" "," "
        while ip1==" " or 0 <= ip1 or ip1 > 9:
            ip1 = int(input("Enter the place no for inserting(X): "))
            print("Enter a valid place!!!" ) if 0 <= ip1 or ip1 > 9 else update_board(board,ip1,ip2)
        if win_check(board)==True: 
            gameover=True
            print(p1," Wins !!!!")
            break
        while ip2==" " or 0 <= ip2 or ip2 > 9:
            ip2 = int(input("Enter the place no for inserting(O): "))
            print("Enter a valid place!!!" ) if 0 <= ip2 or ip2 > 9 else update_board(board,ip1,ip2)
        if win_check(board) == True:
            gameover = True
            print(p2, " Wins !!!!")
            break
main()
