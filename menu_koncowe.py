import pygame
import button
import os
import time

pygame.init()

screen_width=1500
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("END")

game=False
menu_state = "menu3"

class Healtbar():


    def __init__(self, max_health, position_x, position_y, text, image_name):
        self.max_health = max_health
        self.current_health = max_health
        self.x = position_x
        self.y = position_y
        self.text = text

        image_path = os.path.join("postacie", image_name)
        self.image = pygame.image.load(image_path) 
        self.image = pygame.transform.scale(self.image, (40, 40))  

        self.start_time = time.time()  # czas rozpoczęcia = aktualny czas
        self.dlugosc_rundy = 60  # runda = 60 sekund, chyba wystarczy tyle
        self.koniec_timera = False  # to zeby rozumiec ze timer się zakończył

        self.winner = None # tego potrzebuje zeby w koncu rundy sie pojawialo okienko z informacja kto tam wygral 
        #self.pokaz_opcje = False  # to ma sie zmienic na True kiedy timer sie skonczy, dla wyswirtlania opcji


    def update(self, current_health_player1, current_health_player2):
        self.current_health_player1 = current_health_player1
        self.current_health_player2 = current_health_player2

        czas_uplyniety = time.time() - self.start_time
        if  czas_uplyniety >= self.dlugosc_rundy:
            self.koniec_timera = True
            #self.pokaz_opcje = True  # tu sie wlasnie zmienia na True



        # tu sprawdzam czy czas timera się skończył
        czas_uplyniety = time.time() - self.start_time
        if  czas_uplyniety >= self.dlugosc_rundy:
            self.koniec_timera = True


            # chyba wygrywa ten, kto ma wiecej zdrowia na koniec rundy
            if self.current_health_player1 > self.current_health_player2:
                self.winner = "Player 1"
            elif self.current_health_player1 < self.current_health_player2:
                self.winner = "Player 2"
            else:
                self.winner = "Remis"




    def draw_healthbar(self, screen):
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y, 350, 40))
        pygame.draw.rect(screen, (255,0,100), (self.x+25, self.y+5, int((self.current_health*300/self.max_health)),30))
        pygame.draw.rect(screen, (0,0,0),(self.x+360, self.y, 40, 40))
        screen.blit(self.image, (self.x + 360, self.y))

        font = pygame.font.Font('freesansbold.ttf', 32)
        render = font.render(self.text, True, (0,0,0))
        screen.blit(render,(self.x,self.y-35))

        if self.koniec_timera and self.winner:
        # ta czesc dla wyswietlania wynikow
            wynik_text = f"{self.winner} wygrał!"
            wynik_font = pygame.font.Font('freesansbold.ttf', 40)
            wynik_render = wynik_font.render(wynik_text, True, (255, 255, 255))
            wynik_rect = wynik_render.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
            pygame.draw.rect(screen, (0, 0, 0), (wynik_rect.left - 10, wynik_rect.top - 10, wynik_rect.width + 20, wynik_rect.height + 20))
            pygame.draw.rect(screen, (255, 0, 0), wynik_rect)
            screen.blit(wynik_render, wynik_rect.topleft)



tlo_img = pygame.image.load("Button1/czarny_kwadrat (3) 2.jpg").convert_alpha()
tlo=button.Button(460, 120, tlo_img, 1)
background_img=pygame.image.load("Button1/BG2.JPEG").convert_alpha()
quit_img = pygame.image.load("Button1/5397d2da22b328d (1).png").convert_alpha()
quit_button=button.Button(610, 500, quit_img, 1)
replay_img = pygame.image.load("Button1/replay (1).png").convert_alpha()
replay_button=button.Button(580, 200, replay_img, 1)

run=True
koniec_timera = True  # to zeby rozumiec ze timer się zakończył
winner=Healtbar()
winner.update()

while run: 
    screen.fill((1,1,20))
    screen.blit(background_img,(0,0))
    if game==True:
        pass
    if tlo.draw(screen):
        menu_state = "menu3"
    elif quit_button.draw(screen):
        menu_state="menu3"
    elif replay_button.draw(screen):
        menu_state="menu3"
    elif koniec_timera and winner:
        # ta czesc dla wyswietlania wynikow
            wynik_text = f"{winner} wygrał!"
            wynik_font = pygame.font.Font('freesansbold.ttf', 40)
            wynik_render = wynik_font.render(wynik_text, True, (255, 255, 255))
            wynik_rect = wynik_render.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            pygame.draw.rect(screen, (0, 0, 0), (wynik_rect.left - 10, wynik_rect.top - 10, wynik_rect.width + 20, wynik_rect.height + 20))
            pygame.draw.rect(screen, (255, 0, 0), wynik_rect)
            screen.blit(wynik_render, wynik_rect.topleft)




    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game=True
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()

pygame.quit()
