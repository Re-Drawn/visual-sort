import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
import random

pygame.init()

class ArrElement(pygame.sprite.Sprite):
    arr = []

    def __init__(self, value):
        super(ArrElement, self).__init__()
        self.value = value
        self.surf = pygame.Surface((5, self.value))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        ArrElement.arr.append(self)

    @staticmethod
    def shuffle():
        random.shuffle(ArrElement.arr)
    
    @staticmethod
    def clear():
        for i in ArrElement.arr:
            del i

def update_display():
    display.fill((0,0,0))

    for i in range(len(ArrElement.arr)):
        display.blit(ArrElement.arr[i].surf, (i*6, 100))
    
    pygame_widgets.update(pygame.event.get())
    pygame.display.flip()


# Initialization
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 500
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
slider = Slider(display, 0,0, 100, 10, max=100, step=1)

for i in range(1, 101):
    ArrElement(i)

running = True

# Main loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_display()

    clock.tick(60)

pygame.quit()