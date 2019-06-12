# Player 1 is X
# Player 2 is O

import os


gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1Moves = []
player2Moves = []
whosTurn = 1


def clear():
    return os.system("cls")


def drawGameboard():

    print(f" {gameboard[0]} │ {gameboard[1]} │ {gameboard[2]} ")
    print(u"───┼───┼───")
    print(f" {gameboard[3]} │ {gameboard[4]} │ {gameboard[5]} ")
    print(u"───┼───┼───")
    print(f" {gameboard[6]} │ {gameboard[7]} │ {gameboard[8]} ")


def userInput():
    global whosTurn

    # Player 1's turn
    if whosTurn == 1:
        print()
        move = input("Player 1 where would you like to go? ")

        if move == "":
            return

        if gameboard[int(move)] != " ":
            print("Cannot go in that space.")
            return

        player1Moves.append(move)
        gameboard[int(move)] = "X"
        whosTurn = 2
    elif whosTurn == 2:
        print()
        move = input("Player 2 where would you like to go? ")

        if move == "":
            return

        if gameboard[int(move)] != " ":
            print("Cannot go in that space.")
            return

        player2Moves.append(move)
        gameboard[int(move)] = "O"
        whosTurn = 1


def isGameOver():
    if gameboard[0] == "O" and gameboard[1] == "O" and gameboard[2] == "O":
        return


def main():
    while " " in gameboard:
        clear()
        drawGameboard()
        userInput()


if __name__ == '__main__':
    main()
