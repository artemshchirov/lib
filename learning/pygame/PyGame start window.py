import pygame, sys


size = (510, 510)
screen = pygame.display.set_mode(size)  # Создание и задание размера окна
pygame.display.set_caption('Моя программа')
# img = pygame.image.load('name.png')  # Переменная к img для иконки
# pygame.display.set_icon(img)  # Установить иконку
width = height = 40
red = (255, 0, 0)
white = (255, 255, 255)

margin = 10  # Для отступов в рисовании
mas = [[0] * 10 for i in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Захват клавиш мыши
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x_mouse={x_mouse}, y_mouse={y_mouse}')
            column = x_mouse // (margin+width)
            row = y_mouse // (margin+height)
            mas[row][column] ^= 1

    for row in range(10):
        for col in range(10):
            if (mas[row][col] == 1):
                color = red
            else:
                color = white
            x = col * width + (col + 1) * margin
            y = row * height + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, width, height))  # Вывод на экран: (экран, rgb, (x coord, y coord, width, height))

    pygame.display.update()
