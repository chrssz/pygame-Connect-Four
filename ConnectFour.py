from Negamax import negaMax #import negamax algorithm
from GameStatus import GameStatus
import pygame

#GameBoard for connect four.
class ConnectFour:
    def __init__(self, size = (600,600)):
        self.size = self.width, self.height = size
        #Color Definition
        self.WHITE = (255,255,255)
        self.RED = (255,0,0) 
        self.YELLOW = (255,247,0)
        self.BLUE = (0,85,255)
        self.BLACK = (0,0,0)
        #Board list
        self.board = [[0 for _ in range(7)] for _ in range(6)] #6 x 7 board game for connect four.
        self.ROW_COUNT = 6 
        self.COL_COUNT = 7
        #Constant Vars for Grid SIZE
        self.SQUARE_SIZE = 100 
        self.GRID_WIDTH = self.COL_COUNT * self.SQUARE_SIZE
        self.GRID_HEIGHT = (self.ROW_COUNT + 1) * self.SQUARE_SIZE
        self.screen = pygame.display.set_mode(size)
        self.RADIUS = 45 #Radius of discs
        self.cell_width = 100
        self.cell_height = 100

        
    #function responsible for drawing game to screen
    def draw_game(self):
        #init pygame
        pygame.init()

        self.screen.fill(self.WHITE)
        #draw board game
        for col in range(self.COL_COUNT):
            for row in range(self.ROW_COUNT):
                #Display blue border
                pygame.draw.rect(self.screen, self.BLUE, (col * self.SQUARE_SIZE, row* self.SQUARE_SIZE+self.SQUARE_SIZE,self.SQUARE_SIZE,self.SQUARE_SIZE))
                #Display Empty cells
                pygame.draw.circle(self.screen, self.WHITE, (int(col * self.SQUARE_SIZE + self.SQUARE_SIZE / 2), int(row * self.SQUARE_SIZE + self.SQUARE_SIZE + self.SQUARE_SIZE / 2)), int(self.SQUARE_SIZE / 2 - 5)) 

      
        pygame.display.update()

    #draws red disc
    def draw_red(self,column, row):
        x_center = column * self.cell_width + self.cell_width / 2
        y_center = row * self.cell_height + self.cell_height / 2
        #pygame.draw.circle(self.screen, self.RED, (int(x_center), int(y_center)), self.radius)
        #pygame.draw.circle(self.screen, self.RED, (column,row), self.RADIUS)
    
    
    #draws yellow disc
    def draw_yellow(self,column,row):
        pygame.draw.circle(self.screen, self.YELLOW, (column,row), self.RADIUS)
       
    

    def play_game(self):
        done = False
        self.game_state = GameStatus(self.board, True)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()




#Main
Connect_four_game = ConnectFour()
Connect_four_game.draw_game()
Connect_four_game.play_game()


       
        



