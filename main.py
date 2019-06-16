# Player 1 is X
# Player 2 is O

import random
import os


def clear():
    return os.system("cls")


gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1Moves = []
player2Moves = []
whosTurn = 1


class player():
    moves = []
    moveCount = 0

    def __init__(self):
        super().__init__()

    def generateValidMove(self):
        moves = self.moves

        i = True
        while i == True:  # Keep going until it generates a random gameboard location that is empty
            # Generates 1 random number from 0 to 8
            r = random.randint(0, 8)
            if gameboard[r] is " ":  # Is the randomly selected gameboard location empty?
                moves.append(r)  # Add r to the player's moves list
                i = False  # If it is then end the while loop because r is a valid number
                print(f"Your new move is {r}")

    def nextMove(self):
        moves = self.moves
        moveCount = self.moveCount

        if len(moves) is 0:  # Is the player's moves empty
            self.generateValidMove()

        # Used to keep creating new moves if the moves list is empty.
        if moves[moveCount] is None:
            self.generateValidMove()

        if len(moves) > 0:
            moveCount = moveCount + 1
            # Return the next move from the list. This is the rightmost number in the list
            return moves[len(moves) - 1]


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

        if validMove(move) == False:
            return

        player1Moves.append(move)
        gameboard[int(move)] = "X"
        whosTurn = 2
    elif whosTurn == 2:
        print()
        move = input("Player 2 where would you like to go? ")

        if validMove(move) == False:
            return

        player2Moves.append(move)
        gameboard[int(move)] = "O"
        whosTurn = 1


def playerInput(player1, player2):
    global whosTurn

    # Player 1's turn
    if whosTurn == 1:
        # print()
        #move = input("Player 1 where would you like to go? ")
        move = player1.nextMove()

        if validMove(move) == False:
            print("Player 1: ")
            return

        # player1Moves.append(move)
        gameboard[int(move)] = "X"
        whosTurn = 2
    elif whosTurn == 2:
        # print()
        #move = input("Player 2 where would you like to go? ")
        move = player2.nextMove()

        if validMove(move) == False:
            print("Player 2: ")
            return

        # player2Moves.append(move)
        gameboard[int(move)] = "O"
        whosTurn = 1


def validMove(move):
    if move == "":
        return False

    if int(move) > len(gameboard):
        return False

    if gameboard[int(move)] != " ":
        print("Cannot go in that space.")
        return False
    return True


def isGameOver(player1, player2):
    # Rows
    if gameboard[0] == "O" and gameboard[1] == "O" and gameboard[2] == "O":
        player2
    if gameboard[0] == "X" and gameboard[1] == "X" and gameboard[2] == "X":
        player1

    if gameboard[3] == "O" and gameboard[4] == "O" and gameboard[5] == "O":
        player2
    if gameboard[3] == "X" and gameboard[4] == "X" and gameboard[5] == "X":
        player1

    if gameboard[6] == "O" and gameboard[7] == "O" and gameboard[8] == "O":
        player2
    if gameboard[6] == "X" and gameboard[7] == "X" and gameboard[8] == "X":
        player1

    # Columns
    if gameboard[0] == "O" and gameboard[3] == "O" and gameboard[6] == "O":
        player2
    if gameboard[0] == "X" and gameboard[3] == "X" and gameboard[6] == "X":
        player1

    if gameboard[1] == "O" and gameboard[4] == "O" and gameboard[7] == "O":
        player2
    if gameboard[1] == "X" and gameboard[4] == "X" and gameboard[7] == "X":
        player1

    if gameboard[2] == "O" and gameboard[5] == "O" and gameboard[8] == "O":
        player2
    if gameboard[2] == "X" and gameboard[5] == "X" and gameboard[8] == "X":
        player1

    # Diagonals
    if gameboard[0] == "O" and gameboard[4] == "O" and gameboard[8] == "O":
        player2
    if gameboard[0] == "X" and gameboard[4] == "X" and gameboard[8] == "X":
        player1

    if gameboard[2] == "O" and gameboard[4] == "O" and gameboard[6] == "O":
        player2
    if gameboard[2] == "X" and gameboard[4] == "X" and gameboard[6] == "X":
        player1

    return None


def main():
    playerList = []
    winners = []

    # Create the players
    # The number of players needs to be an even number
    for i in range(2):
        p = player()
        playerList.append(p)
        print(f"Created player {i}")

    # Play the games
    for i in range(0, len(playerList), 2):
        player1 = playerList[i]
        player2 = playerList[i + 1]

        winner = None
        while " " in gameboard and winner is None:
            clear()
            drawGameboard()
            # userInput()
            playerInput(player1, player2)
            winner = (isGameOver(player1, player2))
        clear()
        drawGameboard()
        winners.append(winner)
        print()
        print(f"The winners are {winners}.")
        print()

        j = 0
        for p in playerList:
            print(f"Player {j}'s moves {p}")
            j = j + 1

        #print(f"Player 1's moves {player1Moves}")
        #print(f"Player 2's moves {player2Moves}")


if __name__ == '__main__':
    main()
