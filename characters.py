import pygame
import os
from math import log

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
            self.__facing = 'right'
        elif self.__controlled_by == 1:
            super().__init__(850, 666-size)
            self.__facing = 'left'
        ###
        
        ### Ta część wyznacza hitboxy postaci
        self.__heigh, self.__width = size, size/2
        self.upper_hitbox = pygame.Rect(self.get_position()[0],self.get_position()[1],self.__width, self.__heigh/2)
        self.lower_hitbox = pygame.Rect(self.get_position()[0], self.get_position()[1] + self.__heigh/2, self.__width, self.__heigh/2)
        self.hitboxes = [self.upper_hitbox, self.lower_hitbox]
        self.attacks = []
        ###            
            
        ### Ta część ustawia makysmalne i początkowe statystyki postaci
        self.__max_hit_points = hp
        self.__hit_points = hp
        self.__max_stamina = stamina
        self.__stamina = stamina
        self.__speed = speed ### 
        ###
        
        ### Ustawia grafikę postaci
        self.__sprite_list = sprite
        self.__sprite_id = 0
        ###

        ### Tu będą różna potencjalne, stany postaci
        self.__stun = 0
        self.__attacking = 0
        self.__jumping = 0
        self.__crouching = 0
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
    
    def get_speed(self):
        return self.__speed
    
    def get_stunned(self):
        if self.__stun > 0:
            return True
        else:
            return False

    def get_sprite(self):
        sprite = pygame.image.load(os.path.join('postacie', self.__sprite_list[self.__sprite_id]))
        if self.__facing == "left":
            sprite = pygame.transform.flip(sprite,1,0)
        return sprite
        
    def move(self, x, y = 0):
        x = int(x)
        y = int(y)
        if self.get_position()[1] + y > 666 - self.__heigh:
            y = 666 - self.__heigh - self.get_position()[1]
        if x < 0:
            if self.get_position()[0] < -x:
                x = -self.get_position()[0]
        elif x + self.get_position()[0] + self.__width > 1280:
            x = 1280 - self.get_position()[0] - self.__width
        super().move(x,y)
        self.lower_hitbox = self.lower_hitbox.move(x,y)
        self.upper_hitbox = self.upper_hitbox.move(x,y)
    
    ### Sprawdza w dość prymitwyny spośob, czy postać dotyka ziemi
    def Grounded(self):
        if self.get_position()[1] >= 666 - self.__heigh:
            return True
        else:
            return False
        
    def tire(self, value):
        self.__stamina -= value
        if self.__stamina < 0:
            self.__stamina = 0
    
    def Jump(self):
        self.tire(5)
        self.__jumping = 8
        self.lower_hitbox = self.lower_hitbox.move(0, - self.__heigh/4)

    def crouch(self):
        if not self.__crouching:
            self.upper_hitbox = self.upper_hitbox.move(0, self.__heigh/2)
        self.__crouching = 2
        self.__sprite_id = 1
    
    ### Ustawia pozycje postaci i przemieszcza je zgodnie z grawitacją
    def adjust(self,dt, facing):
        if self.__stun:
            self.__stun -= 1
        else:
            self.__stamina += 1

        if self.__jumping:
            self.move(0,- self.__jumping * 100 * dt)
            self.__jumping -= 1
            if self.__jumping == 0:
                self.lower_hitbox = self.lower_hitbox.move(0, self.__heigh/4)
        elif not self.Grounded():
            self.move(0, 300*dt)

        
        if self.__crouching:
            self.__crouching -= 1
            if not self.__crouching:
                self.upper_hitbox = self.upper_hitbox.move(0, - self.__heigh/2)
                self.__sprite_id = 0
        
        if facing > self.get_position()[0]:
            self.__facing =   'right'
        else:
            self.__facing = 'left'
        
        if self.__attacking:
            self.__attacking -= 1
            if not self.__attacking:
                self.attacks = []
                self.__sprite_id = 0
        self.hitboxes = [self.upper_hitbox, self.lower_hitbox]
    
    
    ### Zadaje postaci knockback i obrażenia
    def hit(self, damage, knockback = 0):
        self.__hit_points -= int(damage * log(self.__max_stamina, self.__stamina+2))
        if self.__hit_points < 0:
            self.__hit_points = 0 
        if self.__facing == 'right':
            self.move(-knockback,-knockback)
        else:
            self.move(knockback,knockback)
#######
##Miejsce na metody ataków
    def basic_kick(self):
        position = self.lower_hitbox.center
        position = list(position)
        self.__stun = 15 - self.__speed
        self.__attacking = 15 - self.__speed
        self.tire(10)
        if self.__facing == 'right':
            position[0] = position[0] + int(self.__width/2)
            kick = pygame.Rect(position[0],position[1] , 30, 15)
        else:
            position[0] = position[0] - int(self.__width/2)
            kick = pygame.Rect(position[0]-30,position[1], 30, 15)
        self.attacks.append(kick)
        self.__sprite_id = 3
    
    def basic_punch(self):
        position = self.upper_hitbox.center
        position = list(position)
        self.__stun = 15 - self.__speed
        self.__attacking = 15 - self.__speed
        self.tire(10)
        if self.__facing == 'right':
            position[0] = position[0] + int(self.__width/2)
            punch = pygame.Rect(position[0],position[1] , 30, 15)
        else:
            position[0] = position[0] - int(self.__width/2)
            punch = pygame.Rect(position[0]-30,position[1], 30, 15)
        self.attacks.append(punch)
        self.__sprite_id = 2

#### Postacie
class Presets():
    def __init__(self,hp, stamina, speed, size, sprite):
        self.__hp = hp
        self.__stamina = stamina 
        self.__speed = speed
        self.__size = size 
        self.__sprite = sprite
    def create(self):
        return self.__hp, self.__stamina, self.__speed, self.__size, self.__sprite

Liszy = Presets(200,200, 6, 80, ["liszy_standing.png", 'liszy_crouch.png', 'liszy_punch.png','liszy_kick.png'])
Ninja = Presets(160,200,9,80,["ninja_standing.png", 'ninja_crouch.png', 'ninja_punch.png','ninja_kick.png'])
Grol = Presets(300,300, 5, 100, ["grol_standing.png", 'grol_crouch.png', 'grol_punch.png','grol_kick.png'])
Billy = Presets(90, 60, 10, 60, ["billy_standing.png", 'billy_crouch.png', 'billy_punch.png','billy_kick.png'])
