import pygame
import sys
import newtraining

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (130,238,134)
FONT_SIZE = 36

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Menu with Buttons')
font = pygame.font.Font(None, FONT_SIZE)

# Define button properties
button_width, button_height = 300, 50
button1_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 - 60, button_width,
                           button_height)
button2_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 + 60, button_width,
                           button_height)


def draw_button(rect, text, color):
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, color, rect)
    label = font.render(text, True, WHITE)
    screen.blit(label,(rect.x + (rect.width - label.get_width()) // 2, rect.y + (rect.height - label.get_height()) // 2))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(event.pos):
                    newtraining.main1()
                    return#simply makes sure that the program doesnt draw the screen after the training is done
                elif button2_rect.collidepoint(event.pos):
                    print("Button 2 clicked!")

        screen.fill((50, 150, 200))

        draw_button(button1_rect, 'TRAIN NEW MODEL', BUTTON_COLOR)
        draw_button(button2_rect, 'USE EXISTING MODEL', BUTTON_COLOR)

        pygame.display.flip()


if __name__ == "__main__":
    main()