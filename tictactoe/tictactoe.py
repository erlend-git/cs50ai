"""
Tic Tac Toe Player
"""

import math
import copy
import random
import time

X = "X"
O = "O"
EMPTY = None




class Node:
    def __init__(self, state, parent,action):
        self.state = state
        self.parent = parent
        self.action = action
    


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY,      EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    This functions returns player who has the next turn on a board.
    """
    filled_squares = 0
    for row in board:
        for column in row:
            if column is not EMPTY:
                filled_squares += 1
    
    if filled_squares % 2 == 0:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    available_actions = set()

    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == EMPTY:
                available_actions.add((i,j))


    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    _player = player(board)

    updated_board = copy.deepcopy(board)

    if action not in actions(board):
        raise Exception("Illigal move") 

    updated_board[action[0]][action[1]] = _player

    return updated_board
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    return {1: X, -1: O, 0: None}[utility(board)]
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    Terminal if one player has 3 in a row or diagonal.. or board is full
    
    """
 # # # board[0,1]
 # # #
 # # #

    # Assumes the board is a square matrix of size 3

    if not actions(board):
        return True
    elif utility(board):
        return True
    else:
        return False


        



def print_board(board):
    print("board")

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


    winner = {
        X: 1,
        O: -1,
    }


    # Main diagonal
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
      return winner[board[0][0]]

    # Anti diagonal
    if board[2][0] is not EMPTY and board[2][0] == board[1][1] == board[0][2]:
        return winner[board[2][0]]

  
    for i in range(3):

        # Horizontal check
        if board[i][0] is not EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return winner[board[i][0]]
        # Vertical check
        if board[0][i] is not EMPTY and board[0][i] == board[1][i] == board[2][i]:
            return winner[board[0][i]]
    

    return 0

     
search_history = []

depth = 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    def minvalue(depth,boardstate):
        
        if(terminal(boardstate)):
            return utility(boardstate)
        depth += 1
        results = []

        v = float("inf")
        for action in actions(boardstate):
            maxval = maxvalue(depth,result(boardstate,action))
            v = min(v,maxval)
            results.append(maxval)
        print("MIN - Depth:", depth,"Actions:",  len(actions(boardstate)),"Chosen v: ",v,"Chosen v: ",v, "Results: ", str(results))
        return v

    # Utforsk mulighetene
    # Søk etter vinnerbrett
    # Hva er det beste trekket?
        # Trekket som fører til største vinner mulighetene 
        # 

    def maxvalue(depth, boardstate):
        
        

        
        if(terminal(boardstate)):
            print("")
            drawboard(boardstate)
            u = utility(boardstate)
            return u
        depth += 1    
        v = float("-inf")

       

        for action in actions(boardstate):
            minval = minvalue(depth,result(boardstate,action))
            v = max(v,minval)
            
        
        
        return v

    moves = []
    computer_player = player(board)
    for action in actions(board):
        new_boardstate = result(board,action)
        next_player = player(new_boardstate)
        if terminal(new_boardstate):
            if winner(new_boardstate) == computer_player:
              return None
        print("Current result:", str(moves))
        if next_player == X:
          moves.append([action,maxvalue(0,new_boardstate)])
        if next_player == O:
          moves.append([action,minvalue(0,new_boardstate)])

    print("Final result b4 sort:", str(moves))
    is_max_player = player(board) == X
    moves.sort(key=lambda x: x[1], reverse=is_max_player)
    print("Final result:", str(moves))
    next_action = moves[0][0]
    

    return next_action
    
    return random.choice(list((actions(board))))

     

   

    


        


def drawboard(board):

    result=""

    for row in board:
        result += "|"
        for col in row:
            if col == None:
                result += "   "
            else:
                result += " " + col + " "
        result += "|\n"

    print(result)


    






    
