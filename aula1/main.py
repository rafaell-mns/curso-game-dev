import pygame
import time
import random

def desenho_teste():
    window.blit(font.render('Chess', False, (0,0,0)), (170,40))
    pygame.draw.rect(window, (0,0,0), pygame.Rect(300,150,50,50))
    pygame.draw.rect(window, (0,0,0), pygame.Rect(250,200,50,50))
    pygame.draw.rect(window, (0,0,0), pygame.Rect(200,150,50,50))
    pygame.draw.rect(window, (0,0,0), pygame.Rect(300,250,50,50))
    pygame.draw.rect(window, (0,0,0), pygame.Rect(200,250,50,50))

def atualiza_cor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

screen_width = 800  # largura
screen_height = 600 # altura

pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.Font('aula1/cream-beige.ttf', 60)

running = True

quadrado = {
    "x": 100,
    "y": 100,
    "size": 140
}

velocidadeX = 35
velocidadeY = 35

r, g, b = 0, 0, 160 # cor inicial

while running:
    pygame.draw.rect(window, (0,0,0), pygame.Rect(0,0,screen_width, screen_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # desenho_teste()
    
    pygame.draw.rect(window, (r,g,b), pygame.Rect(quadrado["x"], quadrado["y"], quadrado["size"], quadrado["size"]))

    texto = font.render('DVD', True, (255, 255, 255))
    text_rect = texto.get_rect(center=(quadrado["x"] + quadrado["size"] // 2, quadrado["y"] + quadrado["size"] // 2))
    window.blit(texto, text_rect)

    quadrado["x"] += velocidadeX
    quadrado["y"] += velocidadeY
    
    if quadrado["x"] + quadrado["size"] >= screen_width or quadrado["x"] <= 0:
        velocidadeX *= -1
        r, g, b = atualiza_cor()
        
    if quadrado["y"] + quadrado["size"] >= screen_height or quadrado["y"] <= 0:
        velocidadeY *= -1
        r, g, b = atualiza_cor()

    pygame.display.update()
    time.sleep(0.16)
