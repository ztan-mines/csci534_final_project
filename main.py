#!/usr/local/bin/python3

import pygame
import colors
from tetris import Tetris
from tetromino import Tetromino
from shapes import Shapes

res = (800, 1080)

def main():
    res = (800, 1500)  # TODO: global var
    tetris = Tetris()
    pygame.init()
    screen = pygame.display.set_mode(res)
    done = False
    while not done:

        # check end conditions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # draw background
        screen.fill(colors.WHITE)

        # add new tetromino
        tetris.tetrominos.append(Tetromino(Shapes.I, 0, 1))
        # update occupancy
        for tetromino in tetris.tetrominos:
            for i in range(tetromino.row, tetromino.row + 4):
                for j in range(tetromino.col, tetromino.col + 4):
                    if tetromino.shape[i-4][j-4].is_occupied:
                        tetris.board[i][j].is_occupied = True
                        tetris.board[i][j].color = tetromino.shape[i-4][j-4].color
                        print(i, j)

        # draw board
        for i in range(tetris.board_height):
            for j in range(tetris.board_width):

                # draw grid
                pygame.draw.rect(
                    screen, 
                    colors.GRAY, 
                    [
                        tetris.grid_x + tetris.square_width * j, 
                        tetris.grid_y + tetris.square_width * i, 
                        tetris.square_width, 
                        tetris.square_width
                    ], 
                    1
                )

                # draw tetrominos
                """
                for ea tetromino
                    start at start location
                        for each row and column, draw color if occupied
                """
                if tetris.board[i][j].is_occupied:
                    pygame.draw.rect(
                        screen,
                        tetris.board[i][j].color,
                        [
                            tetris.grid_x + tetris.square_width * j + 1,
                            tetris.grid_y + tetris.square_width * i + 1,
                            tetris.square_width - 2,
                            tetris.square_width - 1
                        ]
                    )

        # update drawings
        pygame.display.flip()
  

if __name__ == "__main__":
    main()