import chess, chess.engine
from random import randint


# todo: give bot a double var (0, 1) for every (is_) variable, which is the weight of each (is_)
#   multiply all the weights together for each move, with every
'''
initialization 
'''

board = chess.Board()
move_count = 0

'''
defining how it picks moves
'''

engine = chess.engine.SimpleEngine.popen_uci(r"Stockfish/stockfish-windows-x86-64-avx2.exe")


def player_turn():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)


def bot_turn():
    legal_moves = list(board.legal_moves)
    for potential_move in legal_moves:  # needs to use neurons to determine how good these moves are
        pass
    try:
        result = legal_moves[0]  # find literally any way to calculate this other than random
    except IndexError:
        return
    board.push(result)


'''
begin game
'''

if randint(0, 1) == 0:  # if randint is 1, give the player the white pieces - otherwise, the bot gets them
    bot_turn()

while not board.is_game_over():
    player_turn()
    bot_turn()

print("Game over.")
print(board)
