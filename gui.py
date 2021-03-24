"""GUI for the Sudoku Puzzle"""

import sys, pygame as pg
import sudoku

pg.init()
screen_size = 430, 450
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 40)

obj = sudoku.Sudoku(9, 2)
grid = obj.main()

def draw_background():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 400, 400), 5, 8)

    i = 1
    while i * 45 <= 400:
        line_width = 2 if i % 3 != 0 else 5
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 45) + 12, 15), pg.Vector2((i * 45) + 12 , 414), line_width)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 45) + 12), pg.Vector2(414, (i * 45) + 12), line_width)
        i += 1

def draw_numbers():
    row = 0
    offset = 32
    while row < 9:
        col = 0
        while col < 9:
            if grid[row][col] != 0:
                output = grid[row][col]
            else:
                output = " "
                
            n_text = font.render(str(output), True, pg.Color("black"))
            screen.blit(n_text, pg.Vector2((col * 44) + offset, (row * 44) + offset - 5))
            
            col += 1

        row += 1

def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    draw_background()
    draw_numbers()
    pg.display.flip()


while True:
    game_loop()

