import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
import time
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort

class ArrElement(pygame.sprite.Sprite):
    arr = []
    element_pos = []

    def __init__(self, value):
        super(ArrElement, self).__init__()
        self.value = value
        self.surf = pygame.Surface((15, self.value*7))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        ArrElement.element_pos.append(self)
        ArrElement.arr.append(self)

    @staticmethod
    def shuffle():
        random.shuffle(ArrElement.element_pos)
    
    @staticmethod
    def clear():
        for i in ArrElement.arr:
            del i


def update_display(elements = None):
    display.fill((0,0,0))

    if not elements:
        for i in range(len(ArrElement.element_pos)):
            display.blit(ArrElement.element_pos[i].surf, (i*16, 900-ArrElement.element_pos[i].value*7))
    
    pygame_widgets.update(pygame.event.get())
    pygame.display.flip()


def sort():
    int_arr = []
    for i in ArrElement.element_pos:
        int_arr.append(i.value)

    result, comparisons, swaps = bubble_sort(int_arr)
    swap_count = 0

    for comparison in comparisons:
        ArrElement.element_pos[comparison[0]].surf.fill((255,0,0))
        ArrElement.element_pos[comparison[1]].surf.fill((255,0,0))
        if swap_count < len(swaps) and comparison == swaps[swap_count]:
            ArrElement.element_pos[comparison[0]], ArrElement.element_pos[comparison[1]] = ArrElement.element_pos[comparison[1]], ArrElement.element_pos[comparison[0]]
            swap_count += 1
        update_display()
        ArrElement.element_pos[comparison[0]].surf.fill((255,255,255))
        ArrElement.element_pos[comparison[1]].surf.fill((255,255,255))
        # TODO: Allow changes in speed mid-sort
        time.sleep(0.01)

# Initialization
pygame.init()
DISPLAY_WIDTH = 1600
DISPLAY_HEIGHT = 900
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
shuffle_button = Button(display, 1500, 0, 100, 70, text = 'Shuffle', onClick = ArrElement.shuffle)
sort_button = Button(display, 1400, 0, 100, 70, text='Sort', onClick = sort)

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
