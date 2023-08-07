from tkinter import font
import pygame

pygame.init()

screen_width = 800
screen_height = 600 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

font = pygame.font.SysFont("arialblack", 40)

text_colour = (255,255, 255)



def draw_text (text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:

    screen. fill((17, 64, 150))


    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()