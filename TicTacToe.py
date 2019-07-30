import random
import os
import argparse
import csv
import json
from TreeModel import Node, Model
from time import process_time_ns

gameboard = []
global_moves = []
playerList = []
winners = []
whosTurn = -1

# Argument handler
parser = argparse.ArgumentParser()

parser.add_argument(
    "--winners", help="Prints all the winning players and their moves along with their gameboard.", action="store_true")
parser.add_argument(
    "--players", help="Prints all the players and their moves", action="store_true")
parser.add_argument("--games", help="How many game should be played", type=int)
parser.add_argument(
    "--count", help="Display the current game number", action="store_true")
parser.add_argument(
    "--board", help="Display the game board", action="store_true")

args = parser.parse_args()


def clear():
    return os.system("cls")


class Strategy(object):
    def __init__(self, moves, wins, losses):
        super().__init__()
        self.moves = moves
        self.wins = wins
        self.losses = losses

    def getWinPercentage(self):
        return self.wins / (self.wins + self.losses)


class StrategyList(object):
    def __init__(self, number):
        super().__init__()
        self.number = number
        filename = (f"players/player{number}.csv")
        self.filename = filename
        self.strategies = []

        # Create a new file for each player to store personalized data
        stratFile = open(filename, "w+")
        stratFile.close()

    def loadFile(self):
        self.strategies = []

        with open(self.filename, "r") as stratFile:
            reader = csv.reader(stratFile)
            for row in reader:
                newStrat = Strategy(row[0], row[1], row[2])
                self.strategies.append(newStrat)

    def saveFile(self):
        with open(self.filename, "w") as stratFile:
            writer = csv.writer(stratFile)
            for strategy in self.strategies:
                writer.writerow(strategy.moves, strategy.wins, strategy.losses)

    def createStrategy(self, moves=None, wins=0, losses=0):
        self.loadFile()

        newStrat = Strategy(moves, wins, losses)
        self.strategies.append(newStrat)

        self.saveFile()

    def getStragegy(self, number):
        for strategy in self.strategies:
            if strategy.number is number:
                return strategy


class player(object):

    def __init__(self, number):
        super().__init__()
        self.number = number

        # myStrats = strategyList(number)
        # self.myStrats = myStrats

        if number % 2 is 0:
            self.letter = "X"
        else:
            self.letter = "O"

        self.moves = []
        self.moveCount = 0
        self.currentStrategy = 0
        self.wins = 0
        self.losses = 0

        self.ml = Model()
        print(f"Created Model for player{number}")

    def generateValidMove(self):
        i = True
        while i is True:  # Keep going until it generates a random gameboard location that is empty
            # Generates 1 random number from 0 to 8
            r = random.randint(0, 8)
            if gameboard[r] is " ":  # Is the randomly selected gameboard location empty?
                self.moves.append(r)  # Add r to the player's moves list
                i = False  # If it is then end the while loop because r is a valid number
                # print(f"Your new move is {r}")

    # def findBestMove(self, node):

    def nextMove(self):
        # ***************** Pick the best move from based on the model *****************
        nd = self.ml.data
        for bp in global_moves:
            for c in nd.children:
                if bp == c.board_pos:
                    nd = c
                    # print(f"Found end: {nd.board_pos}")

        best_node = None
        if all(n.rank == nd.children[0].rank for n in nd.children):
            selection = nd.children[random.randint(
                0, len(nd.children) - 1)].board_pos
            # print("Random Selection: " + str(selection))
            return selection

        else:
            for i in nd.children:
                if best_node == None or i.rank > best_node.rank:
                    best_node = i

            selection = best_node.board_pos
            # print("Highest Ranked Position: " + str(selection))
            r = random.randint(1, 100)
            if r < 60:
                return selection
            else:
                return nd.children[random.randint(0, len(nd.children) - 1)].board_pos

        '''
        if len(self.moves) is 0:  # Is the player's moves empty
            self.generateValidMove()

        # Used to keep creating new moves if the moves list is empty.
        if len(self.moves) is self.moveCount:
            self.generateValidMove()

        if len(self.moves) > 0:
            self.moveCount = self.moveCount + 1
            # Return the next move from the list. This is the rightmost number in the list
            return self.moves[len(self.moves) - 1]
        '''

    def updateModel(self, didIWin):
        if didIWin:
            self.wins = self.wins + 1
        else:
            self.losses = self.losses + 1

        nd = self.ml.data
        for bp in global_moves:
            for c in nd.children:
                if bp == c.board_pos:
                    nd = c

                    if didIWin:
                        nd.rank = nd.rank + 1
                        nd.wins = nd.wins + 1
                    else:
                        nd.rank = nd.rank - 1
                        nd.losses = nd.losses + 1
                    # print(f"Found end: {nd.board_pos}")

    def printModel(self):
        with open(f"player{self.number}Model.txt", "w+", newline="", encoding="UTF-8") as printfile:
            printfile.write(f"Wins: {self.wins}\n")
            printfile.write(f"Losses: {self.losses}\n")
            printfile.write("\n")
            self.ml.printTree(self.ml.data, printfile, "")


class game(object):

    def __init__(self, winner=None, gameboard=[], global_moves=[]):
        super().__init__()
        self.winner = winner
        self.gameboard = gameboard
        self.global_moves = global_moves


def drawGameboard(gb):
    # gb stands for gameboard

    print(f" {gb[0]} │ {gb[1]} │ {gb[2]} ")
    print(u"───┼───┼───")
    print(f" {gb[3]} │ {gb[4]} │ {gb[5]} ")
    print(u"───┼───┼───")
    print(f" {gb[6]} │ {gb[7]} │ {gb[8]} ")


'''
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
'''


def playerInput(player1, player2):
    global whosTurn

    # Player 1's turn
    if whosTurn == 1:
        # print()
        # move = input("Player 1 where would you like to go? ")
        move = player1.nextMove()

        if validMove(move) == False:
            print("Player 1: ")
            return

        # player1Moves.append(move)
        gameboard[int(move)] = player1.letter
        global_moves.append(int(move))
        whosTurn = 2
    elif whosTurn == 2:
        # print()
        # move = input("Player 2 where would you like to go? ")
        move = player2.nextMove()

        if validMove(move) == False:
            print("Player 2: ")
            return

        # player2Moves.append(move)
        gameboard[int(move)] = player2.letter
        global_moves.append(int(move))
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
    p1L = player1.letter
    p2L = player2.letter

    # Rows
    if gameboard[0] == p1L and gameboard[1] == p1L and gameboard[2] == p1L:
        return player1
    if gameboard[0] == p2L and gameboard[1] == p2L and gameboard[2] == p2L:
        return player2

    if gameboard[3] == p1L and gameboard[4] == p1L and gameboard[5] == p1L:
        return player1
    if gameboard[3] == p2L and gameboard[4] == p2L and gameboard[5] == p2L:
        return player2

    if gameboard[6] == p1L and gameboard[7] == p1L and gameboard[8] == p1L:
        return player1
    if gameboard[6] == p2L and gameboard[7] == p2L and gameboard[8] == p2L:
        return player2

    # Columns
    if gameboard[0] == p1L and gameboard[3] == p1L and gameboard[6] == p1L:
        return player1
    if gameboard[0] == p2L and gameboard[3] == p2L and gameboard[6] == p2L:
        return player2

    if gameboard[1] == p1L and gameboard[4] == p1L and gameboard[7] == p1L:
        return player1
    if gameboard[1] == p2L and gameboard[4] == p2L and gameboard[7] == p2L:
        return player2

    if gameboard[2] == p1L and gameboard[5] == p1L and gameboard[8] == p1L:
        return player1
    if gameboard[2] == p2L and gameboard[5] == p2L and gameboard[8] == p2L:
        return player2

    # Diagonals
    if gameboard[0] == p1L and gameboard[4] == p1L and gameboard[8] == p1L:
        return player1
    if gameboard[0] == p2L and gameboard[4] == p2L and gameboard[8] == p2L:
        return player2

    if gameboard[2] == p1L and gameboard[4] == p1L and gameboard[6] == p1L:
        return player1
    if gameboard[2] == p2L and gameboard[4] == p2L and gameboard[6] == p2L:
        return player2

    return None


def printPlayers():
    print()
    print("All the players: ")
    for p in playerList:
        print(f"Player {p.number} was {p.letter} with moves {p.moves}")


def printWinners(player1, player2):
    print()
    '''
    print("The winners are: ")
    for g in winners:
        print(
            f"Player {g.winner.number} was {g.winner.letter} with moves {g.winner.moves}")
        print()
        drawGameboard(g.gameboard)
        print()

    print(f"There were {len(winners)} winners.")
    print(f"There were {args.games - len(winners)} tie games.")
    '''

    print(f"Player1 stats: Wins = {player1.wins}, Losses = {player1.losses}.")
    print(f"Player2 stats: Wins = {player2.wins}, Losses = {player2.losses}.")


def createPlayers():
    # Create the players
    # The number of players needs to be an even number
    for i in range(args.games * 2):
        if not os.path.exists("players"):
            os.makedirs("players")

        p = player(i)
        playerList.append(p)
        # clear()
        print(f"Created player {i}")


def resetGame():
    global gameboard
    global whosTurn
    global global_moves

    # Clear the gameboard and randomly chose who will go first
    gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    whosTurn = random.randint(1, 2)
    global_moves = []


def playGame(drawBoard, drawCount, player1, player2):
    global winners

    resetGame()

    # Play the game loop
    winner = None
    while " " in gameboard and winner is None:
        if drawBoard:
            clear()
            drawGameboard(gameboard)
        # userInput()
        playerInput(player1, player2)
        winner = isGameOver(player1, player2)
    if drawBoard:
        clear()
        drawGameboard(gameboard)

    # Tell the players if they won or lost to update their models
    # Ties count as a loss for both players
    player1.updateModel(winner is player1)
    player2.updateModel(winner is player2)

    if False:
        if winner is not None:
            drawGameboard(gameboard)
            print(global_moves)
            print()

    '''
    # If there was a winner then add that player to the winners list
    if winner is not None:
        winningGame = game(winner, gameboard, global_moves)
        winners.append(winningGame)

        # Create an output log file of the gameboard
        # An X is written as "1", an O is written as a "0", an empty space is written as a "-"
        with open("rawgameboard.txt", "a+") as f:
            toWrite = ""

            for entry in gameboard:
                if entry is "X":
                    toWrite = toWrite + "1"
                elif entry is "O":
                    toWrite = toWrite + "0"
                else:
                    toWrite = toWrite + "_"

            f.write(f"{toWrite}\n")
    '''

    '''
    # If the winner is player 1 then create a new stragety for player 1 and 2 but add a win for player 1 and a loss for player 2

    player1.myStrats.createStrategy(player1.moves)
    player2.myStrats.createStrategy(player2.moves)

    if winner is player1:

    elif winner is player2:
    '''


def main():
    global playerList
    global winners

    '''
    t1 = process_time_ns()
    createPlayers()  # Create Players
    elapsed_time1 = process_time_ns() - t1
    '''

    # Players
    player1 = player(1)
    player2 = player(2)

    t2 = process_time_ns()
    for i in range(args.games):
        if i % 10000 == 0:
            print(f"Playing game #{i}")
            drawGameboard(
                list(map(lambda n: n.rank, player1.ml.data.children)))
        playGame(args.board, args.count, player1, player2)  # Play Game
    elapsed_time2 = process_time_ns() - t2

    # Print stuff when done
    # clear()
    if args.players:
        printPlayers()
    if args.winners:
        printWinners(player1, player2)

    print()
    print("***** Done *****")
    # print(f"Created players in {elapsed_time1 / 1e+9} seconds.")
    print(f"Played all games in {elapsed_time2 / 1e+9} seconds.")

    player1.printModel()
    player2.printModel()


if __name__ == '__main__':
    main()
