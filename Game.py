# This is a simple Python program that prints "Hello, World!" to the console
print("Zombie_Survival_Game!")

# Import Pygame library and initialize it
import pygame
import random  # Add this line to import the 'random' module

pygame.init()

# Set up the game window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Set up the game variables
player_x = width // 2
player_y = height // 2
player_speed = 5
player_image = pygame.image.load("C:/Users/ARJUN_VIJAYAN_JASSIYA/Downloads/player.png")
zombie_image = pygame.image.load("C:/Users/ARJUN_VIJAYAN_JASSIYA/Downloads/zombie.png")
zombie_speed = 3
zombie_list = []

# Set up the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Draw the player and zombies
    screen.blit(player_image, (player_x, player_y))
    for zombie_x, zombie_y in zombie_list:
        screen.blit(zombie_image, (zombie_x, zombie_y))

    # Move the zombies towards the player
    for i, (zombie_x, zombie_y) in enumerate(zombie_list):
        dx = player_x - zombie_x
        dy = player_y - zombie_y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        zombie_x += zombie_speed * dx / dist
        zombie_y += zombie_speed * dy / dist
        zombie_list[i] = (zombie_x, zombie_y)

    # Add new zombies at random intervals
    if random.random() < 0.01:
        zombie_x = random.randint(0, width)
        zombie_y = random.randint(0, height)
        zombie_list.append((zombie_x, zombie_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
