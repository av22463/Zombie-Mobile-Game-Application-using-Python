import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Zombie:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image).convert_alpha()

    def move_towards_player(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            dx = dx / dist
            dy = dy / dist
            self.x += dx * self.speed
            self.y += dy * self.speed

class GameEngine:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(screen_width // 2, screen_height // 2)
        self.zombies = [
            Zombie(100, 100, 2, "C:/Users/ARJUN_VIJAYAN_JASSIYA/Downloads/zombie.png"),
            Zombie(200, 200, 3, "C:/Users/ARJUN_VIJAYAN_JASSIYA/Downloads/player.png")
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.player.move(5, 0)
        if keys[pygame.K_UP]:
            self.player.move(0, -5)
        if keys[pygame.K_DOWN]:
            self.player.move(0, 5)

        for zombie in self.zombies:
            zombie.move_towards_player(self.player)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for zombie in self.zombies:
            self.screen.blit(zombie.image, (int(zombie.x), int(zombie.y)))
        pygame.draw.circle(self.screen, (255, 0, 0), (self.player.x, self.player.y), 10)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    engine = GameEngine(800, 600)
    engine.run()
