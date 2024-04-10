#This python file contains code for the Negamax algorithm
from GameStatus import GameStatus
def negaMax(game_state:GameStatus, depth: int, turn_multiplier: int, alpha = float('-inf'), beta=float('inf')) -> tuple[int,tuple]:
    #first we check if game is terminal or depth = 0
    terminal = game_state.is_terminal()
    if depth == 0 or terminal:
        scores = game_state.get_negamax_scores(terminal) #grab the scores and return (will propagate back up)
        return scores, None
    
    best_move = None
    value = float('-inf')
    
    # checks possible valid moves
    for move in game_state.get_moves():
        # make a move and get new state
        new_state = game_state.get_new_state(move)
        print(f"Negamax making move at: {move}")
        
        # recursively call negamax with inverted values
        new_val, _ = negaMax(new_state, depth - 1, -1 * turn_multiplier, -1 * beta, -1 * alpha)
        
        # undo move
        new_state.undo_move(move)
        
        # negate value. represents opponent's turn
        new_val *= -1
        
        # update best value and move
        if new_val > value:
            value = new_val
            best_move = move
            print(f"Best Value updated: {value}")
            print(f"Best Move updated: {move}")
            
        # apply alpha-beta pruning
        alpha = max(alpha, value)
        if alpha >= beta:
            break

    # if best move is found return inverted value, best_move; else return inverted value, game_state.get_moves()[0]
    return (-1 * value * turn_multiplier, best_move) if best_move is not None else (-1 * value * turn_multiplier, game_state.get_moves()[0])

    