## Import data
import pygame
import os
import pickle
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Define font
font = pygame.font.SysFont("Bauhaus 93", 70)
font_score = pygame.font.SysFont("Bauhaus 93", 30)

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

os.chdir("..")

## define game variables
tile_size = 50
game_over = 0
main_menu = True
level = 0
max_levels = 7
score = 0

## Load assets
sun_img = pygame.image.load(os.path.join("assets", "img", "sun.png"))
bg_img = pygame.image.load(os.path.join("assets", "img", "sky.png"))
restart_img = pygame.image.load(os.path.join("assets", "img", "restart_btn.png"))
start_img = pygame.image.load(os.path.join("assets", "img", "start_btn.png"))
exit_img = pygame.image.load(os.path.join("assets", "img", "exit_btn.png"))


# Function to reset level
def reset_level(level):
    player.reset(100, SCREEN_HEIGHT - 130)
    blobs_group.empty()
    lava_group.empty()
    exit_group.empty()

    # load in level data and create world
    if os.path.exists(os.path.join("my-learn", "level", f"level{level}_data")):
        pickle_in = open(os.path.join("my-learn", "level", f"level{level}_data"), "rb")
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


## Config
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

WHITE = (255, 255, 255)

# Set window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platforming")


def draw_grid():
    for line in range(0, SCREEN_WIDTH // tile_size):
        pygame.draw.line(
            screen, WHITE, (0, line * tile_size), (SCREEN_WIDTH, line * tile_size)
        )
        pygame.draw.line(
            screen, WHITE, (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT)
        )


class World:
    def __init__(self, data):
        self.tile_list = []

        # Load images
        dirt_img = pygame.image.load(os.path.join("assets", "img", "dirt.png"))
        grass_img = pygame.image.load(os.path.join("assets", "img", "grass.png"))

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    blobs_group.add(blob)

                if tile == 6:
                    lava = Lava(
                        col_count * tile_size, row_count * tile_size + (tile_size // 2)
                    )
                    lava_group.add(lava)
                if tile == 7:
                    coin = Coin(
                        col_count * tile_size + (tile_size // 2),
                        row_count * tile_size + (tile_size // 2),
                    )
                    coin_group.add(coin)
                if tile == 8:
                    exit = Exit(
                        col_count * tile_size, row_count * tile_size - (tile_size // 2)
                    )
                    exit_group.add(exit)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # Get Mouse position
        position = pygame.mouse.get_pos()

        # Check mouseover and clicked
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        # Check left mouse be unpressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button
        screen.blit(self.image, self.rect)
        return action


class Player:
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cd = 5

        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[K_SPACE] == False:
                self.jumped = False
            if key[K_a]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[K_d]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[K_a] == False and key[K_d] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # Handle Animation
            if self.counter > walk_cd:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # Add Gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # Check for collision
            self.in_air = True
            for tile in world.tile_list:
                # Check for collision in y direction
                if tile[1].colliderect(
                    self.rect.x + dx, self.rect.y, self.width, self.height
                ):
                    dx = 0

                # Check for collision in y direction
                if tile[1].colliderect(
                    self.rect.x, self.rect.y + dy, self.width, self.height
                ):
                    # Check if below the ground i.e Jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # Check if above the ground i.e falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            if pygame.sprite.spritecollide(self, blobs_group, False):
                game_over = -1

            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            # Update Play coordinate
            self.rect.x += dx
            self.rect.y += dy
        elif game_over == -1:
            self.image = self.dead_img
            draw_text(
                "GAME OVER!", font, BLUE, (SCREEN_WIDTH // 2) - 200, SCREEN_HEIGHT // 2
            )
            if self.rect.y > 200:
                self.rect.y -= 5

        # Draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(1, 5):
            player_img_right = pygame.image.load(
                os.path.join("assets", "img", f"guy{num}.png")
            )
            player_img_right = pygame.transform.scale(player_img_right, (40, 80))
            player_img_left = pygame.transform.flip(player_img_right, True, False)
            self.images_right.append(player_img_right)
            self.images_left.append(player_img_left)

        self.dead_img = pygame.image.load(os.path.join("assets", "img", "ghost.png"))
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("assets", "img", "blob.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.direction
        self.move_counter += 1

        if abs(self.move_counter) > 50:
            self.direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(os.path.join("assets", "img", "lava.png"))
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(os.path.join("assets", "img", "coin.png"))
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(os.path.join("assets", "img", "exit.png"))
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


blobs_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

world_data = []
# Load in level data and create world
if os.path.exists(os.path.join("my-learn", "level", f"level{level}_data")):
    pickle_in = open(os.path.join("my-learn", "level", f"level{level}_data"), "rb")
    world_data = pickle.load(pickle_in)
world = World(world_data)

player = Player(100, SCREEN_HEIGHT - 130)

# Create dummy coin
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

# Create buttons
restart_button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100, restart_img)
start_button = Button(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2, start_img)
exit_button = Button(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2, exit_img)

## Main
running = True

while running:
    clock.tick(fps)

    # update background
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    # Loading Game
    if main_menu == True:
        if start_button.draw() == True:
            main_menu = False

        if exit_button.draw() == True:
            running = False
    else:
        world.draw()

        if game_over == 0:
            blobs_group.update()
            # Update score
            # Check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1

            draw_text("X " + str(score), font_score, WHITE, tile_size - 10, 10)

        blobs_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        # Check if player died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                player.reset(100, SCREEN_HEIGHT - 130)
                game_over = 0
                score = 0

        # Check if player win
        if game_over == 1:
            # Reset game and go to next level
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text(
                    "YOU WIN!",
                    font,
                    BLUE,
                    (SCREEN_WIDTH // 2) - 140,
                    SCREEN_HEIGHT // 2,
                )
                if restart_button.draw():
                    level = 1
                    # reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            running = False

    # Update the display
    pygame.display.update()

pygame.quit()
