import pygame

pygame.init()  # Инициализация экрана. Всегда писать в программе
size = (600, 400)
screen = pygame.display.set_mode(size)
x, y= 0, 300
font = pygame.font.SysFont('cambria', 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock() # FPS

follow = font.render('Тестовый text 1 2 3', 1, RED, GREEN)  # .render(текст, сглаживание (1 - есть, 0 - нет), цвет, фон)
like = font.render('Hello! Тест 321', 1, GREEN, BLUE)  # .render(текст, сглаживание (1 - есть, 0 - нет), цвет, фон)
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit()

    clock.tick(10)  # .tick(кадров/сек)
    screen.blit(follow, (0, 0))  # .blit(screen_name, (x coord, y coord)) - приклепляет к экрану
    screen.blit(like, (x, y))
    x += 1
    pygame.display.update()
