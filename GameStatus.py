#File Contains the gameStatus Class and its methods.

class GameStatus:
    def __init__(self,board_state, turn):
        self.board_state = board_state
        self.turn = turn
        #Constants
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
     
