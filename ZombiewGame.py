import pygame
import random

# Initialize game constants
WIDTH = 800
HEIGHT = 600
UNIT_SIZE = 10

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define the Thing class
class Thing:
    def __init__(self, category, row, col):
        self.category = category
        self.row = row
        self.col = col

# Create an empty grid
grid = [[None for _ in range(WIDTH // UNIT_SIZE)] for _ in range(HEIGHT // UNIT_SIZE)]

# Initialize things
things = []
for _ in range(10):
    row = random.randint(0, HEIGHT // UNIT_SIZE - 1)
    col = random.randint(0, WIDTH // UNIT_SIZE - 1)
    thing = Thing('zombie', row, col)
    things.append(thing)
    grid[row][col] = thing

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move things
    for thing in things:
        if thing.category == 'zombie':
            thing.row += random.choice([-1, 0, 1])
            thing.col += random.choice([-1, 0, 1])
            thing.row = max(0, min(thing.row, HEIGHT // UNIT_SIZE - 1))
            thing.col = max(0, min(thing.col, WIDTH // UNIT_SIZE - 1))

    # Clear the screen
    screen.fill(BLACK)

    # Draw things on the grid
    for thing in things:
        if thing.category == 'zombie':
            pygame.draw.rect(screen, RED, (thing.col * UNIT_SIZE, thing.row * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()
