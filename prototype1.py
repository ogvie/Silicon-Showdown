# Import necessary modules
import pygame, sys
from button import Button  # Assuming a Button class is defined in a module called "button"
from os import path

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Load background image
BG = pygame.image.load("/Users/ogvie/Desktop/Silicon Showdown/background.png")

# Function to get a font with a specified size
def get_font(size):
    return pygame.font.Font("/Users/ogvie/Desktop/Silicon Showdown/LEMONMILK-Bold.otf", size)

# Function for the PLAY screen
def play():
    while True:
        # Get mouse position
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Fill the screen with a black color
        SCREEN.fill("black")

        # Render and display the text for the PLAY screen
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Create a BACK button using the Button class
        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

        # Function for the OPTIONS screen
def options():
    while True:
        # Get mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Fill the screen with a white color
        SCREEN.fill("white")

        # Render and display the text for the OPTIONS screen
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Create a BACK button using the Button class
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Function for the MAIN MENU
def main_menu():
    while True:
        # Fill the screen with a blue color
        SCREEN.fill(("#2a9df4"))
        
        # Get mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Render and display the text for the MAIN MENU
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Define buttons for PLAY, OPTIONS, and QUIT
        PLAY_BUTTON = Button(image=pygame.image.load("/Users/ogvie/Desktop/Silicon Showdown/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("/Users/ogvie/Desktop/Silicon Showdown/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("/Users/ogvie/Desktop/Silicon Showdown/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # Display menu text and update button colors
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Start the main menu loop
main_menu()


