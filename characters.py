
class Character():
        ### Tworzenie postaci
    def __init__(self, hp, stamina, speed , size, sprite, player):
        
        ### Przypisuje postaci do konkretnego gracza
        self.__controlled_by = player
        ###
        
        ### Ustawia początkową pozycję postaci, wartości tymczasowe zmienię jak będzie już zrobione środowisko gry
        if self.__controlled_by == 0:
            self.position = [15,0]
        else:
            self.position = [31, 0]
        ###
        
        ### Ta część będzie wyznaczać hitboxy postaci, póki co jeszcze nie zdefiniowane
        self.__heigh, self.__width = size, size/2
        #self.upper_hitbox = Hitbox(self.heigh, self.width)
        #self.lower_hitbox = Hitbox(self.heigh, self.width)
        ###            
            
        ### Ta część ustawia makysmalne i początkowe statystyki postaci
        self.__max_hit_points = hp
        self.__hit_points = hp
        self.__max_stamina = stamina
        self.__stamina = stamina
        self.__speed = speed ### 
        ###
        
        ### Będzie przypisywać konkretną grafikę psotaci, póki co nie robi nic
        self.__sprite = sprite
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

    def get_speed(self):
        return self.__speed
    
    def get_stunned(self):
        return self.__stunned
    
