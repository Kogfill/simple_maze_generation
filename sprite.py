import pygame

class Sprite:
    all_sprites = []
    tile_size = 20
    screen = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = None

        self.all_sprites.append(self)

    def get_rect(self):
        return pygame.Rect(
            self.x * self.tile_size,
            self.y * self.tile_size,
            self.tile_size,
            self.tile_size
        )

    def on_event(self, event):
        pass

    def update(self):
        pass



class Player(Sprite):
    COLOR = (255, 0, 0)
    START_TIMER = 30
    HOLD_TIMER = 5
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hold = None
        self.timer = 0

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.pressed(event.key)
            self.hold = event.key
            self.timer = self.START_TIMER
        elif event.type == pygame.KEYUP:
            if event.key == self.hold:
                self.hold = None

    def pressed(self, key):
        if key == pygame.K_w:
            d = (0, -1)
        elif key == pygame.K_s:
            d = (0, 1)
        elif key == pygame.K_a:
            d = (-1, 0)
        elif key == pygame.K_d:
            d = (1, 0)
        else:
            return
        next_pos = (self.x + d[0], self.y + d[1])

        if next_pos in Wall.all_walls:
            return

        self.x = next_pos[0]
        self.y = next_pos[1]

    def update(self):
        if self.timer > 0:
            self.timer -= 1
        elif self.timer == 0:
            self.pressed(self.hold)
            self.timer = self.HOLD_TIMER
        
    def draw(self):
        pygame.draw.rect(self.screen, self.COLOR, self.get_rect())
        

class Wall(Sprite):
    all_walls_sp = []
    all_walls = []
    COLOR = (0, 0, 0)
    mg = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.all_walls_sp.append(self)
        self.all_walls.append((x, y))

    @classmethod
    def del_all(cls):
        cls.all_walls = []
        cls.all_walls_sp = []

    @staticmethod
    def from_maze(maze):
        for (y, row) in enumerate(maze):
            for (x, i) in enumerate(row):
                Wall(x, y) if i else None

    def draw(self):
        pygame.draw.rect(self.screen, self.COLOR, self.get_rect())

class Win(Sprite):
    COLOR = (0, 255, 0)
    def __init__(self, x, y, player):
        super().__init__(x, y)
        self.won = False
        self.player = player

    def is_win(self):
        self.won = (self.x == self.player.x) and (self.y == self.player.y)
        return self.won

    def draw(self):
        pygame.draw.rect(self.screen, self.COLOR, self.get_rect())