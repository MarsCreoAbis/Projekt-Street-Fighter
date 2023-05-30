import pygame


class Healtbar():


    def __init__(self, max_health, position_x, position_y):
        self.max_health = max_health
        self.current_health = max_health
        self.x = position_x
        self.y = position_y

    def update(self, current_health):
        self.current_health = current_health

    def draw_healthbar(self, screen):
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y, 350, 40))
        pygame.draw.rect(screen, (255,0,100), (self.x+25, self.y+5, int((self.current_health*300/self.max_health)),30))

        