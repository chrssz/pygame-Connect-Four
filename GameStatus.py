#File Contains the gameStatus Class and its methods.

class GameStatus:
    def __init__(self,board_state, turn):
        self.board_state = board_state
        self.turn = turn
        #Constants
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
    
    #get all valid moves in current game state
    def get_moves(self):
        moves = []
        for x in range(self.ROW_COUNT):
            for y in range(self.COL_COUNT):
                #0 represents empty cells
                if self.board_state[x][y] == 0:
                    moves.append((x,y))
        
        return moves
    #creates new game state based on a given move
    def get_new_state(self,move):
        new_board_state = self.board_state.copy()
        x,y = move[0],move[1]
        new_board_state[x][y] = 1 if self.turn else 2 #1 for player, 2 for AI
        return GameStatus(new_board_state,not self.turn)
    
    #undo move
    def undo_move(self,move):
        self.board_state[move[0]][move[1]] = 0
        self.turn = not self.turn

    #check to see if board is full
    def is_terminal(self):
        for x in range(self.ROW_COUNT):
            for y in range(self.COL_COUNT):
                if self.board_state[x][y] == 0:
                    return False
        
        return True
    #Look for four in a rows.
    def get_negaMax_score(self):
        #Iterate through self.board in reverse order?
            #Worst Case scenario is connect 4 is at the top of the board.
        
        return 
    
        

