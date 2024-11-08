import pygame
import time
import math
import random

def gerar_cor_aleatoria():
    r = random.randint(0, 255)  # Valor de vermelho
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

screen_width = 600
screen_height = 400

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont('Tohama', 40, True, False)

running = True
balls = []
r, g, b = gerar_cor_aleatoria()

while running:
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(0, 0, screen_width, screen_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        vx = random.randint(0, 5)
        vy = random.randint(0, 5)

        if event.type == pygame.MOUSEBUTTONUP:
            coord = event.pos
            pos_x = coord[0]
            pos_y = coord[1]
            print(pos_x)
            balls.append({
                "cor": (r, g, b),
                "x": pos_x,
                "y": pos_y
            })

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                r, g, b = gerar_cor_aleatoria()

    for ball in balls:
        ball['x'] -= random.randint(0, 2)
        ball['y'] += random.randint(0, 2)
        pygame.draw.circle(window, ball["cor"], (ball["x"], ball["y"]), 50)

    pygame.display.update()
    time.sleep(0.05)

pygame.quit()
