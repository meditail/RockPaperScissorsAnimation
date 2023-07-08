import pygame
import random

SIZE = (WIDTH, HEIGHT) = 500, 500
WINDOW = pygame.display.set_mode(SIZE)
WHITE = (255, 255, 255)
SYMBOL_SIZE = (20, 20)
ROCK_IMG = pygame.image.load('./images/rock.jpg')
ROCK_IMG = pygame.transform.scale(ROCK_IMG, SYMBOL_SIZE)
PAPER_IMG = pygame.image.load('./images/paper.jpg')
PAPER_IMG = pygame.transform.scale(PAPER_IMG, SYMBOL_SIZE)
SCISSORS_IMG = pygame.image.load('./images/scissor.jpg')
SCISSORS_IMG = pygame.transform.scale(SCISSORS_IMG, SYMBOL_SIZE)
FPS = 60
COUNT = 50

clock = pygame.time.Clock()
done = False


class Symbol:
    def __init__(self, type):
        self.x = random.randint(SYMBOL_SIZE[0], WIDTH)
        self.y = random.randint(SYMBOL_SIZE[1], HEIGHT)
        self.x_vel = random.randint(-1, 1)
        self.y_vel = random.randint(-1, 1)
        while self.x_vel == 0 or self.y_vel == 0:
            self.x_vel = random.randint(-1, 1)
            self.y_vel = random.randint(-1, 1)
        self.type = type

    def move(self):
        if self.x >= WIDTH or self.x <= 0:
            self.x_vel = -self.x_vel

        if self.y >= HEIGHT or self.y <= 0:
            self.y_vel = -self.y_vel

        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self, window):
        if self.type == 0:
            image = ROCK_IMG
        elif self.type == 1:
            image = PAPER_IMG
        else:
            image = SCISSORS_IMG

        x_pos = self.x - image.get_width() / 2
        y_pos = self.y - image.get_height() / 2

        window.blit(image, (x_pos, y_pos))


symbols = [Symbol(0) for _ in range(COUNT)]
symbols += [Symbol(1) for _ in range(COUNT)]
symbols += [Symbol(2) for _ in range(COUNT)]


def draw():
    WINDOW.fill(WHITE)
    for symbol in symbols:
        symbol.draw(WINDOW)
    pygame.display.update()


def move():
    for symbol in symbols:
        symbol.move()


def collision(symbol_list):
    for i in range(len(symbol_list)):
        for j in range(i, len(symbol_list)):
            if symbol_list[j].x - (SYMBOL_SIZE[0]) < symbol_list[i].x < symbol_list[j].x + (SYMBOL_SIZE[0]) and symbol_list[j].y - (SYMBOL_SIZE[1]) < symbol_list[i].y < symbol_list[j].y + (SYMBOL_SIZE[1]):
                symbol = symbol_list[i]
                other_symbol = symbol_list[j]
                if (symbol.type == 0 and other_symbol.type == 1) or (symbol.type == 1 and other_symbol.type == 2) or (symbol.type == 2 and other_symbol.type == 0):
                    symbol.type = other_symbol.type
                else:
                    other_symbol.type = symbol.type


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    collision(symbols)
    draw()
    move()
    clock.tick(FPS)


