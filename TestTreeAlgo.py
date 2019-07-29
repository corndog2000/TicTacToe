from TreeModel import Node, Model

# Decision Tree Model
ml = Model()
#print(ml.data)

'''
for key, value in ml.data.items():
    print(ml.data[key].board_pos)
    print(ml.data[key].rank)
    print(ml.data[key].children)
'''

global_moves = []

def main():
    global ml

    if global_moves is []:
        for node in ml.data:
            highest_rank = 0
            if node.rank > highest_rank:
                highest_rank = node.board_pos

    for mv in global_moves:
        

        # If the model is empty
    #if all(node == "-1" for node in ml.data):




if __name__ == "__main__":
    main()