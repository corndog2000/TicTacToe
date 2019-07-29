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



    search = True
    temp_moves = global_moves
    current_node = ml.data

    highest_rank = None
    highest_rank_board_pos = None
    
    while search is True:
        if len(temp_moves) == 0:
            if all(value == 0 for value in current_node.values()):  # All of the children of the current node are 0

            for pos in current_node:
                if highest_rank == None or pos.rank > highest_rank:
                    highest_rank = pos.rank
                    highest_rank_board_pos = pos.board_pos

            ## Stop looking for the best move
            search = False
            return highest_rank_board_pos
        else:
            

        # If the model is empty
    #if all(node == "-1" for node in ml.data):




if __name__ == "__main__":
    main()