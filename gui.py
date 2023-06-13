import pygame
import os
import time

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
        self.timer_duration = 60  # runda = 60 sekund, chyba wystarczy tyle
        self.timer_expired = False  # to zeby rozumiec ze timer się zakończył

        self.winner = None # tego potrzebuje zeby w koncu rundy sie pojawialo okienko z informacja kto tam wygral 

    def update(self, current_health_player1, current_health_player2):
        self.current_health_player1 = current_health_player1
        self.current_health_player2 = current_health_player2

        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.timer_duration:
            self.timer_expired = True


        # tu sprawdzam czy czas timera się skończył
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.timer_duration:
            self.timer_expired = True


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

        if self.timer_expired and self.winner:
        # ta czesc dla wyswietlania wynikow
            wynik_text = f"{self.winner} wygrał!"
            wynik_font = pygame.font.Font('freesansbold.ttf', 40)
            wynik_render = wynik_font.render(wynik_text, True, (255, 255, 255))
            wynik_rect = wynik_render.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            pygame.draw.rect(screen, (0, 0, 0), (wynik_rect.left - 10, wynik_rect.top - 10, wynik_rect.width + 20, wynik_rect.height + 20))
            pygame.draw.rect(screen, (255, 0, 0), wynik_rect)
            screen.blit(wynik_render, wynik_rect.topleft)

        # Wyświetlanie pozostałego czasu timera
        font = pygame.font.Font('freesansbold.ttf', 32)
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.timer_duration - elapsed_time)  # Pozostały czas
        timer_text = f"Time: {int(remaining_time)}"  # Formatowanie tekstu
        render = font.render(timer_text, True, (0, 0, 0))
        screen.blit(render, (self.x, self.y+40))

        # Sprawdzanie, czy timer się zakończył
        if self.timer_expired:
            game_over_text = font.render("Time's up!", True, (255, 0, 0))
            screen.blit(game_over_text, (self.x, self.y + 50))

    