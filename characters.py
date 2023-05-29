import pygame


class Movable(): # Nie jestem pewien co do potrzeby tej klasy, ale na razie jest
    def __init__(self, x, y):
        self.__position_x, self.__position_y = x, y

    def move(self, horizontal, vertical = 0):
        self.__position_x += horizontal
        self.__position_y += vertical
    
    def get_position(self):
        return (self.__position_x, self.__position_y)

class Character(Movable):
        ### Tworzenie postaci
    def __init__(self, hp, stamina, speed , size, sprite, player):
        
        ### Przypisuje postaci do konkretnego gracza
        self.__controlled_by = player
        ###
        
        ### Ustawia początkową pozycję postaci, wartości tymczasowe zmienię jak będzie już zrobione środowisko gry
        if self.__controlled_by == 0:
            super().__init__(425, 666-size)
        elif self.__controlled_by == 1:
            super().__init__(850, 666-size)
        ###
        
        ### Ta część wyznacza hitboxy postaci
        self.__heigh, self.__width = size, size/2
        self.upper_hitbox = pygame.Rect(self.get_position()[0],self.get_position()[1],self.__width, self.__heigh/2)
        self.lower_hitbox = pygame.Rect(self.get_position()[0], self.get_position()[1] + self.__heigh, self.__width, self.__heigh/2)
        ###            
            
        ### Ta część ustawia makysmalne i początkowe statystyki postaci
        self.__max_hit_points = hp
        self.__hit_points = hp
        self.__max_stamina = stamina
        self.__stamina = stamina
        self.__speed = speed ### 
        ###
        
        ### Ustawia grafikę postaci
        self.__sprite = pygame.image.load(sprite)
        self.__sprite = pygame.transform.scale(self.__sprite,(self.__width, self.__heigh))
        if self.__controlled_by == 1:
            self.__sprite = pygame.transform.flip(self.__sprite, 1, 0)
        ###

        ### Tu będą różna potencjalne, stany postaci
        self.__stun = 0
        self.__stunned = False
        ###
        
    def get_controlled_by(self):
        return self.__controlled_by
    
    def get_size(self):
        return self.__heigh, self.__width

    def get_max_hit_points(self):
        return self.__max_hit_points

    def get_hit_points(self):
        return self.__hit_points

    def get_max_stamina(self):
        return self.__max_stamina

    def get_stamina(self):
        return self.__stamina

    def get_sprite(self):
        return self.__sprite
    
    def get_speed(self):
        return self.__speed
    
    def get_stunned(self):
        return self.__stunned

    def get_sprite(self):
        return self.__sprite
        
    def move(self, x, y = 0):
        super().move(x,y)
        self.lower_hitbox.move(x,y)
        self.upper_hitbox.move(x,y)
