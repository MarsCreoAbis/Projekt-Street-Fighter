import pygame
import os
import time

#### Podzieliłem klasę healtbar na dwie, jedna - Heltbar opsługuje wyświetlanie hp postaci, druga - timer wyświetlanie się czasu rundy i zwyciężcy 

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

        
    def update(self, health):
        
        self.current_health = health




    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y, 350, 40))
        pygame.draw.rect(screen, (255,0,100), (self.x+25, self.y+5, int((self.current_health*300/self.max_health)),30))
        pygame.draw.rect(screen, (0,0,0),(self.x+360, self.y, 40, 40))
        screen.blit(self.image, (self.x + 360, self.y))

        font = pygame.font.Font('freesansbold.ttf', 32)
        render = font.render(self.text, True, (0,0,0))
        screen.blit(render,(self.x,self.y-35))

        

    
class interfejs():
    
    def __init__(self, player1_max, player2_max, position_x, position_y):
        self.x = position_x
        self.y = position_y
        self.max_health_player1 = player1_max
        self.max_health_player2 = player2_max
        self.start_time = time.time()  # czas rozpoczęcia = aktualny czas
        self.dlugosc_rundy = 60  # runda = 60 sekund, chyba wystarczy tyle
        self.koniec_timera = False  # to zeby rozumiec ze timer się zakończył
        self.winner = None # tego potrzebuje zeby w koncu rundy sie pojawialo okienko z informacja kto tam wygral 
        #self.pokaz_opcje = False  # to ma sie zmienic na True kiedy timer sie skonczy, dla wyswirtlania opcji

    def update(self, health1, health2):
        self.current_health_player1 = health1
        self.current_health_player2 = health2
        # tu sprawdzam czy czas timera się skończył
        czas_uplyniety = time.time() - self.start_time
        if  czas_uplyniety >= self.dlugosc_rundy:
            self.koniec_timera = True


            # chyba wygrywa ten, kto ma wiecej zdrowia na koniec rundy
            if self.max_health_player1//(self.current_health_player1+1) < self.max_health_player2//(self.current_health_player2+1):
                self.winner = "Player 1 wygrał"
            elif self.max_health_player1//(self.current_health_player1+1) > self.max_health_player2//(self.current_health_player2+1):
                self.winner = "Player 2 wygrał"
            else:
                self.winner = "Remis"

        if health1 == 0:
            self.winner = "Player 2 wygrał"
        if health2 == 0:
            self.winner = "Player 1 wygrał"

    def draw(self, screen):
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        if self.winner:
            wynik_text = f"{self.winner}"
            wynik_font = pygame.font.Font('freesansbold.ttf', 40)
            wynik_render = wynik_font.render(wynik_text, True, (255, 255, 255))
            wynik_rect = wynik_render.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 90))
            pygame.draw.rect(screen, (0, 0, 0), (wynik_rect.left - 10, wynik_rect.top - 10, wynik_rect.width + 20, wynik_rect.height + 20))
            pygame.draw.rect(screen, (255, 0, 0), wynik_rect)
            screen.blit(wynik_render, wynik_rect.topleft)


            # wyswietlanie opcji nowa gra i wyjsc kiedy timer sie skonczy ****** not my code, bo nie zdazylam ******
            option_font = pygame.font.Font('freesansbold.ttf', 24)
            option_text_1 = "1. Nowa gra"
            option_text_2 = "2. Wyjscie"
            option_render_1 = option_font.render(option_text_1, True, (0, 0, 0))
            option_render_2 = option_font.render(option_text_2, True, (0, 0, 0))
            option_rect_1 = option_render_1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
            option_rect_2 = option_render_2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80))
            screen.blit(option_render_1, option_rect_1.topleft)
            screen.blit(option_render_2, option_rect_2.topleft)
           

        else:
            # pozycja timera
            timer_x = (self.x + self.x + 350) // 2  # tu licze srodek healtbara 
            timer_y = self.y + 90  # tu zadaje pozycje

            # czas uplyniety
            czas_uplyniety = time.time() - self.start_time
            czas_pozostaly = max(0, self.dlugosc_rundy -  czas_uplyniety)
            timer_text = f"Time: {int(czas_pozostaly)}"
            render = font.render(timer_text, True, (0, 0, 0))
            timer_rect = render.get_rect(center=(timer_x, timer_y))
            screen.blit(render, timer_rect)

            # Sprawdzanie, czy timer się zakończył
            if self.koniec_timera:
                koniec_gry_text = font.render("Czas sie skonczyl", True, (255, 0, 0))
                screen.blit(koniec_gry_text, (self.x, self.y + 40))
