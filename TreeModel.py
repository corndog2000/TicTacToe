import json
import os
        
class Node(object):
    def __init__(self):
        super().__init__()
        #self.left = None
        #self.right = None
        self.children = {}
        self.rank = 0
        self.board_pos = None

class Model(object):
    path = "model.json"

    def __init__(self):
        super().__init__()
        self.data = {"0": "-1", "1": "-1", "2": "-1", "3": "-1", "4": "-1", "5": "-1", "6": "-1", "7": "-1", "8": "-1"}

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