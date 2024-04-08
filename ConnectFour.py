from Negamax import negaMax #import negamax algorithm
from GameStatus import GameStatus
import pygame

#GameBoard for connect four.
class ConnectFour:
    def __init__(self, size = (700,650)):
        self.size = self.width, self.height = size
        #Color Definition
        self.WHITE = (255,255,255)
        self.RED = (255,0,0) 
        self.YELLOW = (255,247,0)
        self.BLUE = (0,85,255)
        self.BLACK = (0,0,0)
        #Board list
        self.ROW_COUNT = 6 
        self.COL_COUNT = 7
        self.board = [[0] * self.COL_COUNT for _ in range(self.ROW_COUNT)]     #6 x 7 board game for connect four.
        #Constant Vars for Grid SIZE
        self.SQUARE_SIZE = 100 
        self.GRID_WIDTH = self.COL_COUNT* self.SQUARE_SIZE
        self.GRID_HEIGHT = (self.ROW_COUNT) * self.SQUARE_SIZE
        self.screen = pygame.display.set_mode(size)
        self.RADIUS = 45 #Radius of discs
        self.cell_width = 100
        self.cell_height = 100
       
        
    #function responsible for drawing game to screen
    def draw_game(self) -> None:
        #init pygame
        pygame.init()
        self.screen.fill(self.WHITE)
        #draw board game
        for col in range(self.COL_COUNT):
            for row in range(self.ROW_COUNT):
                #Display blue border
                pygame.draw.rect(self.screen, self.BLUE, (col * self.SQUARE_SIZE, row* self.SQUARE_SIZE,self.SQUARE_SIZE,self.SQUARE_SIZE))
                #Display Empty cells
                pygame.draw.circle(self.screen, self.WHITE, (int(col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2), int(row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)), int(self.SQUARE_SIZE / 2 - 5))
      
        pygame.display.update()
    #Draws red disc at given position
    def draw_red(self, column) -> None:
        # Check if column is within the valid range
        if 0 <= column < self.COL_COUNT:
            # Find the first empty row from the bottom of the column
            for row in range(self.ROW_COUNT - 1, -1, -1):
                if self.board[row][column] == 0:
                    # Place the disc in the lowest available row
                    self.board[row][column] = 2
                    #Draw the red disc on the screen
                    x_center = column * self.cell_width + self.cell_width // 2
                    y_center = row * self.cell_height + self.cell_height // 2
                    pygame.draw.circle(self.screen, self.RED, (x_center, y_center), self.RADIUS)
                    pygame.display.update()
                    break
  

    
        
    
    
    #draws yellow disc at given position
    def draw_yellow(self,column) -> None:
        # Check if column is within the valid range
        if 0 <= column < self.COL_COUNT:
            # Find the first empty row from the bottom of the column
            for row in range(self.ROW_COUNT - 1, -1, -1):
                if self.board[row][column] == 0:
                    # Place the disc in the lowest available row
                    self.board[row][column] = 1
                    #Draw the red disc on the screen
                    x_center = column * self.cell_width + self.cell_width // 2
                    y_center = row * self.cell_height + self.cell_height // 2
                    pygame.draw.circle(self.screen, self.YELLOW, (x_center, y_center), self.RADIUS)
                    pygame.display.update()
                    break
       
    

    def play_game(self) -> None:
        done = False
        self.game_state = GameStatus(self.board, True)

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: #check for mouse click
                    if event.button == 1: #left mouse button is clicked
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        column = mouse_x // self.SQUARE_SIZE #calculates column index based on mouse position
                        #place the disc.
                        self.draw_red(column)
                        self.print_B()
                        #update gameState

    
    #helper function to print out self.board in a clean order
    def print_B(self) -> None:
        for row in self.board:
            print(row)
        print()



#Main
Connect_four_game = ConnectFour()
Connect_four_game.draw_game()
Connect_four_game.play_game()


       
        



