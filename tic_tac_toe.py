
def create_board(board):
    row1 = "\t|{0}|{1}|{2}|".format(board[0], board[1], board[2])
    row2 = "\t|{0}|{1}|{2}|".format(board[3], board[4], board[5])
    row3 = "\t|{0}|{1}|{2}|".format(board[6], board[7], board[8])
    board = " \n{}\t\t\t|1|2|3|\n\t-------\t\t\t-------\n{}\t\t\t|4|5|6|\n\t-------\t\t\t--------\n{}\t\t\t|7|8|9|".format(
        row1, row2, row3)
    return board

def update_board(bd, p1=" ", p2=" "):
    if bd[p1-1] == " ":
        bd[p1-1] = "X"
    elif bd[p2-1] == " ":
        bd[p2-1] = "O"
    else:
        pass
    return print(create_board(bd))

def win_check(bd):
    i,j="X","O"
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
    elif ((bd[0] == j and bd[1] == j and bd[2] == j) or\
        (bd[3] == j and bd[4] == j and bd[5] == j) or\
            (bd[6] == j and bd[7] == j and bd[8] == j) or\
                (bd[0] == j and bd[3] == j and bd[6] == j) or\
                    (bd[1] == j and bd[4] == j and bd[7] == j) or\
                        (bd[2] == j and bd[5] == j and bd[8] == j) or\
                            (bd[0] == j and bd[4] == j and bd[8] == j) or\
                                (bd[2] == j and bd[4] == j and bd[6] == j)):
                                return True
    else:
        return False



board = [" " for _ in range(9)]


def main():
    p1 = 'player 1'
    p2 = 'player 2'
    print('{} - (X)  {} - (O)'.format(p1, p2))
    print(create_board(board))
    gameover = False
    while not gameover:
        ip1, ip2 = " ", " "
        while ip1 == " ":
            ip1 = int(input("Enter the place no for inserting(X): ").strip())
            print("Enter a valid place!!!") if ip1 <= 0 or ip1 > 9 else update_board(
                board, ip1, ip2)
        if win_check(board) == True:
            gameover = True
            print(p1, " Wins !!!!")
            break
        while ip2 == " ":
            ip2 = int(input("Enter the place no for inserting(O): ").strip())
            print("Enter a valid place!!!") if ip2 <= 0 or ip2 > 9 else update_board(
                board, ip1, ip2)
        if win_check(board) == True:
            gameover = True
            print(p2, " Wins !!!!")
            break


main()
