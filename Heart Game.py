import pygame
import sys
import os

pygame.init()

# Setup window
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Heart")

# Load and scale images
def load_and_scale(name, size):
    path = os.path.join(os.path.dirname(__file__), name)
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)

# ✅ Correct variable names here:
player_img = load_and_scale("alex.png", (40, 40))
heart_img = load_and_scale("heart.png", (30, 30))
bg_img = load_and_scale("grass.png", (640, 480))  # make sure it’s grass.png not .webp

# Rects for collision/movement
player_rect = player_img.get_rect(topleft=(100, 100))
heart_rect = heart_img.get_rect(topleft=(300, 200))

speed = 5
heart_collected = False
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: player_rect.x -= speed
    if keys[pygame.K_d]: player_rect.x += speed
    if keys[pygame.K_w]: player_rect.y -= speed
    if keys[pygame.K_s]: player_rect.y += speed

    if player_rect.colliderect(heart_rect) and not heart_collected:
        heart_collected = True
        print("❤️ You collected the heart!")

    # Draw everything
    screen.blit(bg_img, (0, 0))
    screen.blit(player_img, player_rect)
    if not heart_collected:
        screen.blit(heart_img, heart_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
