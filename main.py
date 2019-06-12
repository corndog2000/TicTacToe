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
    # Rows
    if gameboard[0] == "O" and gameboard[1] == "O" and gameboard[2] == "O":
        return "Player 2"
    if gameboard[0] == "X" and gameboard[1] == "X" and gameboard[2] == "X":
        return "Player 1"

    if gameboard[3] == "O" and gameboard[4] == "O" and gameboard[5] == "O":
        return "Player 2"
    if gameboard[3] == "X" and gameboard[4] == "X" and gameboard[5] == "X":
        return "Player 1"

    if gameboard[6] == "O" and gameboard[7] == "O" and gameboard[8] == "O":
        return "Player 2"
    if gameboard[6] == "X" and gameboard[7] == "X" and gameboard[8] == "X":
        return "Player 1"

    # Columns
    if gameboard[0] == "O" and gameboard[3] == "O" and gameboard[6] == "O":
        return "Player 2"
    if gameboard[0] == "X" and gameboard[3] == "X" and gameboard[6] == "X":
        return "Player 1"

    if gameboard[1] == "O" and gameboard[4] == "O" and gameboard[7] == "O":
        return "Player 2"
    if gameboard[1] == "X" and gameboard[4] == "X" and gameboard[7] == "X":
        return "Player 1"

    if gameboard[2] == "O" and gameboard[5] == "O" and gameboard[8] == "O":
        return "Player 2"
    if gameboard[2] == "X" and gameboard[5] == "X" and gameboard[8] == "X":
        return "Player 1"

    # Diagonals
    if gameboard[0] == "O" and gameboard[4] == "O" and gameboard[8] == "O":
        return "Player 2"
    if gameboard[0] == "X" and gameboard[4] == "X" and gameboard[8] == "X":
        return "Player 1"

    if gameboard[2] == "O" and gameboard[4] == "O" and gameboard[6] == "O":
        return "Player 2"
    if gameboard[2] == "X" and gameboard[4] == "X" and gameboard[6] == "X":
        return "Player 1"

    return None


def main():

    winner = None
    while " " in gameboard and winner == None:
        clear()
        drawGameboard()
        userInput()
        winner = isGameOver()
    clear()
    drawGameboard()
    print(f"The winner is {winner}.")
    print(f"Player 1's moves {player1Moves}")
    print(f"Player 2's moves {player2Moves}")


if __name__ == '__main__':
    main()
