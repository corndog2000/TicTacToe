import json
        
class Node(object):
    def __init__(self):
        super().__init__()
        #self.left = None
        #self.right = None
        self.children = {}
        self.rank = 0
        self.board_pos = None

class Model(object):
    def __init__(self):
        super().__init__()
        self.data = None

    def createModel(self, path):
        with open(path, "w+") as new_model:
            return True

    def loadModel(self, path):
        with open(path, "r") as read_file:
            self.data = json.load(read_file)

    def saveModel(self, path):
        with open(path, "a+") as write_file:
            json.dump(self.data, write_file)

    def addBranch(self, moves):
        return True