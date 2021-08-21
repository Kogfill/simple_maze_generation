import pygame
import time

import mazegen as mg
from sprite import *

BACKGROUND = (125, 125, 125)

def main():
    won = False
    flags = 0

    print()
    msize = int(input("maze size: "))
    win_size = int(input("window size: "))

    Sprite.tile_size = win_size//msize

    pygame.init()
    screen = pygame.display.set_mode((win_size, win_size))

    font = pygame.font.SysFont("Consolas", win_size//10)

    Sprite.screen = screen

    p = Player(1, 1)
    w = Win(msize-2, msize-2, p)

    maze = mg.main(msize)
    Wall.from_maze(maze)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and won:
                    won = False
                    (p.x, p.y) = (1, 1)
                    Wall.del_all()
                    maze = mg.main(msize)
                    Wall.from_maze(maze)

                elif event.key == pygame.K_n:
                    flags ^= pygame.NOFRAME
                    screen = pygame.display.set_mode((win_size, win_size), flags)
                    Sprite.screen = screen
                
                elif event.key == pygame.K_ESCAPE:
                    running = False
            
            for sprite in Sprite.all_sprites:
                sprite.on_event(event)

        screen.fill(BACKGROUND)
        if not w.is_win():
            for sprite in (Sprite.all_sprites+Wall.all_walls_sp):
                sprite.update()
                sprite.draw()
        else:
            won = True
            img = font.render("Congratulations", True, (0, 0, 0))
            rect = img.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(img, rect)
        
        pygame.display.flip()
        time.sleep(0.01)
    
    pygame.quit()


if __name__ == "__main__":
    main()