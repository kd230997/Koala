def extract_sprites(image_path, sprite_width, sprite_height, columns, rows):
    img = Image.open(image_path)
    for row in range(rows):
        for col in range(columns):
            x = col * sprite_width
            y = row * sprite_height
            sprite = img.crop((x, y, x + sprite_width, y + sprite_height))
            sprite.save(f"sprite_{row}_{col}.png")

# Example usage
image_path = "your_sprite_sheet.png"
sprite_width = 32
sprite_height = 32
columns = 8
rows = 6
extract_sprites(image_path, sprite_width, sprite_height, columns, rows)