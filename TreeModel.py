import json
import os
        
class Node(object):
    def __init__(self, children={}, rank=0, board_pos=None):
        super().__init__()
        #self.left = None
        #self.right = None
        self.children = children
        self.rank = rank
        self.board_pos = board_pos

class Model(object):
    path = "model.json"

    def __init__(self):
        super().__init__()
        self.data = {"0": "0", "1": "0", "2": "0", "3": "0", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0"}
        for key, value in self.data.items():
            self.data[key] = Node(board_pos = int(key))

    def modelExists(self, path = path):
        if os.path.exists(path):
            return True
        else:
            return False

    def createModel(self, path = path):
        with open(path, "w+") as new_model:
            return True

    def loadModel(self, path = path):
        if not os.path.exists(path):
            open(path, "w+").close()

        with open(path, "r") as read_file:
            self.data = json.load(read_file)
            return self.data

    def saveModel(self, path = path):
        with open(path, "a+") as write_file:
            json.dump(self.data, write_file)

    def addBranch(self, moves):
        return True