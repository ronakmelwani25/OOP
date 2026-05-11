import pygame
pygame.init()

WIDTH=2000
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()