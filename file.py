
import pygame
from  characters import *
from gui import Healtbar

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

ch1 = Character(100, 100, 10, 75, "placeholder.png", 0)
ch2 = Character(100, 100, 10, 100, "placeholder.png", 1)
gray = (128, 128, 128)
red = (128, 0, 0)

############################################

healtbar_1 = Healtbar(ch1.get_max_hit_points(), 50, 50, "player_1")
healtbar_2 = Healtbar(ch2.get_max_hit_points(), 880, 50, "player_2")


#############################################
# pasek z zyciem

button_color = (0, 255, 0)

font = pygame.font.Font(None, 36)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg = pygame.image.load("bg.jpg")
    bg = pygame.transform.scale(bg,(1280, 720))
    screen.blit(bg, (0, 0))

    screen.blit(ch1.get_sprite(), (ch1.get_position()))
    screen.blit(ch2.get_sprite(), (ch2.get_position()))

#######################################################
# wyzywa sie metoda update, ktora odpowiada za zycie gracza
    healtbar_1.update(ch1.get_hit_points())
    healtbar_1.update(ch2.get_hit_points())

# tworzy sie pasek z zyciem gracza
    healtbar_1.draw_healthbar(screen)
    healtbar_2.draw_healthbar(screen)

#######################################################


    if min(ch1.get_hit_points(), ch2.get_hit_points()) <= 0:
        # "Koniec gry"
        end_game_text = font.render("Koniec gry", True, (255, 0, 0))
        screen.blit(end_game_text, (screen_width // 2 - end_game_text.get_width() // 2, screen_height // 2 - end_game_text.get_height() // 2))

       
        button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
        pygame.draw.rect(screen, button_color, button_rect)
        button_text = font.render("Od nowa", True, (0, 0, 0))
        screen.blit(button_text, (screen_width // 2 - button_text.get_width() // 2, screen_height // 2 + 65 - button_text.get_height() // 2))

        
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(mouse_pos):
            
            ch2._Character__hit_points = ch2.get_max_hit_points()  
            ch1._Character__hit_points = ch1.get_max_hit_points() 
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            ch1.move(0,-300 * dt)
        if keys[pygame.K_s]:
            ch1.move(0,300 * dt)
        if keys[pygame.K_a]:
            ch1.move(-300 * dt, 0)
        if keys[pygame.K_d]:
            ch1.move(300 * dt, 0)
        if keys[pygame.K_q]:
            ch1._Character__hit_points -= 5
        if keys[pygame.K_i]:
            ch2.move(0, -300 * dt)
        if keys[pygame.K_k]:
            ch2.move(0, 300 * dt)
        if keys[pygame.K_j]:
            ch2.move(-300 * dt, 0)
        if keys[pygame.K_l]:
            ch2.move(300 * dt, 0)
        if keys[pygame.K_u]:
            ch2._Character__hit_points -= 5       

  
    pygame.display.flip()

   
    dt = clock.tick(60) / 1000

pygame.quit()
    
