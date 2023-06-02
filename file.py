
import pygame
from  characters import *
from gui import Healtbar

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

debugging = False

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
    
    ### Wyświetla hiboxy postaci
    if debugging:
        for box in ch1.get_hitobxes() + ch2.get_hitobxes():
            pygame.draw.rect(screen,(0,255,0),box)

        for attack in ch1.attacks + ch2.attacks:
            pygame.draw.rect(screen,(255,0,0),attack)

#######################################################
# wyzywa sie metoda update, ktora odpowiada za zycie gracza
    healtbar_1.update(ch1.get_hit_points())
    healtbar_2.update(ch2.get_hit_points())

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
        if not ch1.get_stunned():
            if keys[pygame.K_w] and ch1.Grounded():
                ch1.Jump()
            if keys[pygame.K_a]:
                ch1.move(-300 * dt, 0)
            if keys[pygame.K_d]:
                ch1.move(300 * dt, 0)
            if keys[pygame.K_c]:
                ch1.basic_kick()
            if keys[pygame.K_x]:
                ch1.basic_punch()
        if keys[pygame.K_s] and ch1.Grounded():
                ch1.crouch()

        if not ch2.get_stunned():
            if keys[pygame.K_q]:
                ch1._Character__hit_points -= 5
            if keys[pygame.K_i] and ch2.Grounded():
                ch2.Jump()
            if keys[pygame.K_j]:
                ch2.move(-300 * dt, 0)
            if keys[pygame.K_l]:
                ch2.move(300 * dt, 0)
            if keys[pygame.K_n]:
                ch2.basic_kick()
            if keys[pygame.K_m]:
                ch2.basic_punch()
        if keys[pygame.K_k] and ch2.Grounded():
                ch2.crouch()

#### Sprawdzenie kolizji ataków z graczami                
#############################################
        for attack in ch2.attacks[:]:
            temp = False
            for hitbox in ch1.hitboxes:
                if attack.colliderect(hitbox):
                    ch1.hit(10, 500*dt)
                    temp =True
            if temp:
                ch2.attacks.remove(attack)

        for attack in ch1.attacks[:]:
            temp = False
            for hitbox in ch2.hitboxes:
                if attack.colliderect(hitbox):
                    ch2.hit(10, 500*dt)
                    temp =True
            if temp:
                ch1.attacks.remove(attack)
###########################################

        ch1.adjust(dt,ch2.get_position()[0])
        ch2.adjust(dt,ch1.get_position()[0]) 
  
    pygame.display.flip()

   
    dt = clock.tick(60) / 1000

pygame.quit()
    
