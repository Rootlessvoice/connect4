import pygame
from constants import *
from board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()


    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = 1


    def winner(self):
        return self.board.winner


    def end_game(self):
        self.board.end_screen(self.win);


    def reset(self):
        self._init()


    def draw_piece(self, row, col, player):
        self.board.draw_piece(self.win, row, col, player)
        self.change_turn()


    def current_turn(self):
        return self.turn 


    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1