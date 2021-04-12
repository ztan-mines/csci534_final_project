#!/usr/local/bin/python3

import pygame
import colors
from tetris import Tetris

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