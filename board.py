import pygame
from constants import *
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.winner = " "

    
    def draw_squares(self, win):
        win.fill(YELLOW)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.circle(win, GREY, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), RADIUS+OUTLINE)


    def get_piece(self, row, col):
        return self.board[row][col]


    def end_screen(self, win):
        win.fill(BLACK)

        myfont = pygame.font.SysFont(None, 100)

        # render text
        label = myfont.render(self.winner+" wins", 1, RED)
        win.blit(label, (175, 225))


    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)


    def draw_piece(self, win, row, col, player):
        for i, selected_col in reversed(list(enumerate(self.board))):
            if selected_col[col] == 0:
                self.board[i][col] = player
                break
        
        print(self.board)
        self.check_for_winner(player, win);
        

    def draw(self, win):
        self.draw_squares(win)

        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    whos_piece = self.board[row][col]

                    if whos_piece == 1:
                        turn_color = RED
                    else:
                        turn_color = BLACK

                    pygame.draw.circle(win, turn_color, (col*SQUARE_SIZE+SQUARE_SIZE//2,
                                            row*SQUARE_SIZE+SQUARE_SIZE//2), RADIUS+OUTLINE)   

        if self.winner != " ":
            self.end_screen(win)


    def check_for_winner(self, currentPlayer, win):

        thisPlayer = "Red" if currentPlayer == 1 else "Black"

        #check for vertical win
        for row in range(ROWS-3):
            for col in range(COLS):
                if (self.board[row][col] == currentPlayer) and (self.board[row+1][col] == currentPlayer) and (self.board[row+2][col] == currentPlayer) and (self.board[row+3][col] == currentPlayer):
                    print(thisPlayer+" wins!!")
                    self.winner = thisPlayer

        #check for horizontal win
        for row in range(ROWS):
            for col in range(COLS-3):
                if (self.board[row][col] == currentPlayer) and (self.board[row][col+1] == currentPlayer) and (self.board[row][col+2] == currentPlayer) and (self.board[row][col+3] == currentPlayer):
                    print(thisPlayer+" wins!!")
                    self.winner = thisPlayer


        #check for diagonal down win
        for row in range(ROWS-3):
            for col in range(COLS-3):
                if (self.board[row][col] == currentPlayer) and (self.board[row+1][col+1] == currentPlayer) and (self.board[row+2][col+2] == currentPlayer) and (self.board[row+3][col+3] == currentPlayer):
                    print(thisPlayer+" wins!!")
                    self.winner = thisPlayer

        #check for diagonal up win
        for row in range(ROWS-3):
            for col in range(COLS):
                if (self.board[row][col] == currentPlayer) and (self.board[row+1][col-1] == currentPlayer) and (self.board[row+2][col-2] == currentPlayer) and (self.board[row+3][col-3] == currentPlayer):
                    print (thisPlayer+" wins!!")
                    self.winner = thisPlayer


