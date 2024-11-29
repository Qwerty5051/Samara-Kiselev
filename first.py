import pygame
import random
def draw_square(screen):
    x, y = (random.randrange(0, 800), random.randrange(0, 600))

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = pygame.Color(r, g, b)
    # рисуем "тень"
    pygame.draw.circle(screen, color, (x, y), random.randrange(1, 40))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)

    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:

    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
        draw_square(screen)
    # завершение работы:
    pygame.quit()
