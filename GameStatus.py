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
    def get_negaMax_score(self) -> int:
        scores = {0:0,1:0,2:0} # keep track of scores
        # Check for four in rows horizontally
        for x in range(self.ROW_COUNT):
            for y in range(self.COL_COUNT - 3):
                if (
                    self.board_state[x][y] == self.board_state[x][y+1] ==
                    self.board_state[x][y+2] == self.board_state[x][y+3]):
                    scores[self.board_state[x][y]] += 100

        # Check for four in rows vertically
        for x in range(self.ROW_COUNT - 3):
            for y in range(self.COL_COUNT):
                if (
                    self.board_state[x][y] == self.board_state[x+1][y] ==
                    self.board_state[x+2][y] == self.board_state[x+3][y]):
                    scores[self.board_state[x][y]] += 100

        # Check for four in rows diagonally (bottom-left to top-right)
        for x in range(self.ROW_COUNT - 3):
            for y in range(self.COL_COUNT - 3):
                if (
                    self.board_state[x][y] == self.board_state[x+1][y+1] ==
                    self.board_state[x+2][y+2] == self.board_state[x+3][y+3]):
                    scores[self.board_state[x][y]] += 100

        # Check for four in rows diagonally (top-left to bottom-right)
        for x in range(3, self.ROW_COUNT):
            for y in range(self.COL_COUNT - 3):
                if (
                    self.board_state[x][y] == self.board_state[x-1][y+1] ==
                    self.board_state[x-2][y+2] == self.board_state[x-3][y+3]):
                    scores[self.board_state[x][y]] += 100

        return scores[1] - scores[2]
                    
            
    
    
        

