"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if odd o
    # if even x
    counter = 0
    for x in board:
        for y in x:
            if y == None:
                counter = counter + 1
    if counter % 2 == 0:
        return X
    else:
        return O        
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


winning_states = ["1,2,3",
                   "1,4,7",
                   "1,5,9",
                   "2,5,8",
                   "3,5,7",
                   "3,6,9",
                   "4,5,6",
                   "7,8,9"]

def all_elements_same(array):
    return all(x == array[0] for x in array)

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # find the winner
    board_dict = {}
    counter = 1
    for x in board:
        for y in x:
            board[counter] = y
    
    for state in winning_states:
        for item in state.split(","):
            state_ar = []
            state_ar.append(board_dict[item])
            
            print(state_ar)
            
            if all_elements_same(state_ar):
                return state_ar[0]
    
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #  if all the board is filled then its a terminal state
    
    counter = 0
    for x in board:
        for y in x:
            if y == None:
                counter = counter + 1
    if counter == 0:
        return True
    else:
        if winner(board) == None:
            return False
        else:
            return True
            
        
    
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
