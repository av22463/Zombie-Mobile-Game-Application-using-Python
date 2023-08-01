import pygame

class GameEngine:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.zombie_image = pygame.image.load("C:/Users/ARJUN_VIJAYAN_JASSIYA/Downloads/player.png")  # Load the zombie image

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        # Draw a red rectangle in the center of the screen
        rect_width = 200
        rect_height = 100
        rect_x = (self.screen_width - rect_width) // 2
        rect_y = (self.screen_height - rect_height) // 2
        # Blit the zombie image onto the rectangle
        self.screen.blit(self.zombie_image, (rect_x, rect_y))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    engine = GameEngine(800, 600)
    engine.run()
