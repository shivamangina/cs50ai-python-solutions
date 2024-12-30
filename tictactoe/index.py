from tictactoe import player 

X = "X"
O = "O"
EMPTY = None

board = [[O, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, O]]

result = player(board)

print(result)

