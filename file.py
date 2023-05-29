
import pygame
from  characters import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

ch1 = Character(100, 100, 10, 3, "", 0)
ch2 = Character(100, 100, 10, 4, "", 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    bg = pygame.image.load("bg.jpg")
    screen.blit(bg, (0, 0))

    pygame.draw.circle(screen, "red", pygame.Vector2(ch1.get_position()), 40)
    pygame.draw.circle(screen, "purple", pygame.Vector2(ch2.get_position()), 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ch1.move(0,-300 * dt)
    if keys[pygame.K_s]:
        ch1.move(0,300 * dt)
    if keys[pygame.K_a]:
        ch1.move(-300 * dt, 0)
    if keys[pygame.K_d]:
        ch1.move(300 * dt, 0)
    if keys[pygame.K_i]:
        ch2.move(0, -300 * dt)
    if keys[pygame.K_k]:
        ch2.move(0, 300 * dt)
    if keys[pygame.K_j]:
        ch2.move(-300 * dt, 0)
    if keys[pygame.K_l]:
        ch2.move(300 * dt, 0)
#tu pod ifami można dodać co się ma dziać po kliknięciu
   
    pygame.display.flip()

   
    dt = clock.tick(60) / 1000

pygame.quit()
