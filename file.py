
import pygame
from  characters import *
from gui import Healtbar
import time

class GameRound():
    def __init__(self, ch1, ch2):
        self.points_p1 = self.points_p2 = 0
        self.cycle_state_p1 = ch1._Character__hit_points
        self.cycle_state_p2 = ch2._Character__hit_points
        self.last_hit_time_p1 = None
        self.last_hit_time_p2 = None
        self.p1_combo = 0
        self.p2_combo = 0
        self.cycle_time = time.time()

    def checkCycle(self):
        self.cycle_time = time.time()
        if (d := self.cycle_state_p1 - ch1._Character__hit_points) != 0:
            self.points_p2 += 1 + int(float(f'{d}.{d}')*(0.30*self.p2_combo))
            self.cycle_state_p1 = ch1._Character__hit_points
            if self.last_hit_time_p2 is None:
                self.last_hit_time_p2 = time.time()
            time_now = time.time()
            if time_now - self.last_hit_time_p2 < 1.7:
                self.p2_combo +=1
            self.last_hit_time_p2 = time_now
        if (d := self.cycle_state_p2 - ch2._Character__hit_points) != 0:
            self.points_p1 += 1 + int(float(f'{d}.{d}')*(0.30*self.p1_combo))
            self.cycle_state_p2 = ch2._Character__hit_points
            if self.last_hit_time_p1 is None:
                self.last_hit_time_p1 = time.time()
            time_now = time.time()
            if time_now - self.last_hit_time_p1 < 1.7:
                self.p1_combo +=1
            self.last_hit_time_p1 = time_now
        if self.p1_combo != 0:
            if self.cycle_time - self.last_hit_time_p1 > 1.8:
                self.p1_combo = 0
        if self.p2_combo != 0:                
            if self.cycle_time - self.last_hit_time_p2 > 1.8:
                self.p2_combo = 0
    
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# ta zmienna powinna się zmienić na True, w momencie startu rundy
game_started = False
dt = 0






### Trzeba dodać menu wyboru postaci
choice1 = Liszy.create()
choice2 = Ninja.create()

ch1 = Character(choice1[0],choice1[1],choice1[2],choice1[3],choice1[4], 0)
ch2 = Character(choice2[0],choice2[1],choice2[2],choice2[3],choice2[4], 1)


gray = (128, 128, 128)
red = (128, 0, 0)

############################################
# tu sie tworza obiekty

healtbar_1 = Healtbar(ch1.get_max_hit_points(), 50, 50, "player_1", "player_1.jpg")
healtbar_2 = Healtbar(ch2.get_max_hit_points(), 880, 50, "player_2","player_2.jpg")


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
    
    ### Wyświetla hiboxy postacis
    if debugging:
        for box in ch1.hitboxes + ch2.hitboxes:
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
    # punktacja - mozna przerzucic do GUI - wszytsko sie bedzei naliczac, wystarczy zmnniejszyc hp postaci, w jakikolwiek sposób, im więcej zada na raz, tym więcej punktów dostanie
    tekst = font.render(str(round.points_p1), True, '#ffffff')
    screen.blit(tekst, (460, 60))
    tekst = font.render(str(round.points_p2), True, '#ffffff')
    screen.blit(tekst, (830, 60))

    #licznik combo - mona przerzucic do GUI, wystarczy trafic przeciwnika szybicej niz 1 raz na sekunde
    if round.p1_combo > 2:
        tekst = font.render(str(f'COMBO: {round.p1_combo}'), True, '#ffffff')
        screen.blit(tekst, (110, 120))
    if round.p2_combo > 2:
        tekst = font.render(str(f'COMBO: {round.p1_combo}'), True, '#ffffff')
        screen.blit(tekst, (880, 120))

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

        ch1.adjust(dt,ch2.get_position()[0])
        ch2.adjust(dt,ch1.get_position()[0]) 
  
    pygame.display.flip()

   
    dt = clock.tick(60) / 1000

pygame.quit()
    
