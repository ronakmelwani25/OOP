import pygame
pygame.init()

WIDTH=1900
HEIGHT=1000
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("white")

class rectangle():
    def __init__(self,width,height,x,y,colour,thickness):
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.colour=colour
        self.thickness=thickness
    def draw(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height),self.thickness)

rect1=rectangle(500,300,1200,100,"purple",0)
rect1.draw()

rect2=rectangle(200,400,200,500,"red",1)
rect2.draw()

rect3=rectangle(400,400,700,500,"green",100)
rect3.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()