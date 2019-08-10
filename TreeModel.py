#import json
import os
import pickle


class Node(object):
    def __init__(self, rank=0, board_pos=None):
        super().__init__()
        self.children = []
        #self.rank = rank()
        self.wins = 0
        self.losses = 0
        self.board_pos = board_pos

    def win(self):
        #print("Incrementing Wins")
        self.wins += 1

    def loss(self):
        #print("Incrementing Losses")
        self.losses += 1

    def rank(self):
        if self.wins == 0 or self.losses == 0:
            return 0
        else:
            #print(f"Rank Function Output: {self.wins}, {self.losses}, {self.wins / self.losses}")
            return self.wins / (self.wins + self.losses)


class Model(object):

    def __init__(self, path):
        super().__init__()
        # self.data = {"0": "0", "1": "0", "2": "0", "3": "0", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0"}
        self.data = Node(board_pos=-1)
        self.path = path

        # Recursive function
        def initializeModel(node, available_pos):
            for i in available_pos:
                # There are no more available board positions to assign. Quit the loop.
                if (len(available_pos) <= 0):
                    print(
                        f"Exausted Available Positions. This node has {len(node.children)} children.")
                    return
                # print("***")

                new_node = Node(board_pos=i)
                node.children.append(new_node)
                #print(f"appending node with board position = {new_node.board_pos}")

                new_available_pos = available_pos.copy()
                #print(f"i = {i}")
                new_available_pos.remove(i)
                initializeModel(new_node, new_available_pos)

        # Original size is 9 since the top layer will have 9 nodes
        #size = 9

        # All board positions. Since a tic-tac-toe board has 9 spaces there are 9 positions
        available_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        initializeModel(self.data, available_pos)

        '''
        for i in range(len(available_pos)):

            # I make a local copy for each loop iteration
            local_pos = available_pos
            initializeModel(self.data, local_pos)
        '''

        # for key, value in self.data.items():
        #    self.data[key] = Node(board_pos=int(key))

    def printTree(self, node, path, to_write, level=0, spaces=3):
        '''
        if not level == 0:
            #to_write = ((" " * ((level - 1) * spaces) + u"\u2514" + (u"\u2500" * (spaces - 1)) + str(node.board_pos)) + (f" ({node.rank}, {node.wins}, {node.losses})") + "\n")
            path.write(to_write)
        else:
            #to_write = (str(node.board_pos)) + (f" ({node.rank}, {node.wins}, {node.losses})") + "\n"
            path.write(to_write)
        '''

        if node.board_pos != -1:
            to_write = to_write + str(node.board_pos)
        
        path.write(to_write + (f" ({node.rank()}, {node.wins}, {node.losses})") + "\n")
        
        for i in node.children:
            self.printTree(i, path, to_write, level + 1, spaces)

    def modelExists(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

    def createModel(self, path):
        with open(path, "wb") as new_model:
            return True

    def loadModel(self, path):
        if not os.path.exists(path):
            open(path, "wb").close()

        with open(path, "rb") as read_file:
            self.data = pickle.load(read_file)
            return self.data

    def saveModel(self, path):
        with open(path, "wb") as write_file:
            pickle.dump(self.data, write_file)


if __name__ == "__main__":
    print("This is a helper library. It is not meant to be ran by itself.")
