
class Character():
        ### Tworzenie postaci
    def __init__(self, hp, stamina, speed , size, sprite, player):
        
        ### Przypisuje postaci do konkretnego gracza
        self.controlled_by = player
        ###
        
        ### Ustawia początkową pozycję postaci, wartości tymczasowe zmienię jak będzie już zrobione środowisko gry
        if self.controlled_by == 0:
            self.position = [15,0]
        else:
            self.position = [31, 0]
        ###
        
        ### Ta część będzie wyznaczać hitboxy postaci, póki co jeszcze nie zdefiniowane
        self.heigh, self.width = size, size/2
        #self.upper_hitbox = Hitbox(self.heigh, self.width)
        #self.lower_hitbox = Hitbox(self.heigh, self.width)
        ###            
            
        ### Ta część ustawia makysmalne i początkowe statystyki postaci
        self.max_hit_points = hp
        self.hit_points = hp
        self.max_stamina = stamina
        self.stamina = stamina
        self.speed = 5 - speed ### 
        ###
        
        ### Będzie przypisywać konkretną grafikę psotaci, póki co nie robi nic
        self.sprite = sprite
        ###

        ### Tu będą różna potencjalne, stany postaci
        self.stun = 0
        self.stunned = False
        ###
