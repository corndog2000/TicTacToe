import os
import random
from TreeModel import Node, Model

# Decision Tree Model
ml = Model()
print("Created Model")

# print(ml.data)
#print("Total Children: " + str(len(ml.data.children)))

with open("printTree.txt", "w+", newline="", encoding="UTF-8") as printfile:
    ml.printTree(ml.data, printfile)

global_moves = [0, 1, 2, 3, 4, 5, 6, 7]

nd = ml.data
for bp in global_moves:
    for c in nd.children:
        if bp == c.board_pos:
            nd = c
            print(f"Found end: {nd.board_pos}")

best_node = None
if all(n.rank == nd.children[0].rank for n in nd.children):
    selection = nd.children[random.randint(0, len(nd.children) - 1)].board_pos
    print("Random Selection: " + str(selection))

else:
    for i in nd.children:
        if best_node == None or i.rank > best_node.rank:
            best_node = i

    print("Highest Ranked Position: " + str(best_node.board_pos))

print("Done")
