import pygame
import os
# Load the sprite sheet
sprite_sheet = pygame.image.load(os.path.join("assets", "wizard", "wizard.png"))

# Get the dimensions of the sprite sheet
sheet_width, sheet_height = sprite_sheet.get_rect().size

# Determine the dimensions of a single sprite
sprite_width = sheet_width // 8  # Assuming 4 sprites per row
sprite_height = sheet_height // 8  # Assuming 4 sprites per column

print("Sprite width:", sprite_width)
print("Sprite height:", sprite_height)
