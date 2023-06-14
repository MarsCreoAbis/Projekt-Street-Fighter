#podczas tworzenia kodu korzystałam z kodu oraz wskazówek Coding With Russ ,,How to Create a Menu in Pygame" oraz plik, który nazywa się Button pochodzi w całości od niego i jedynie usunełam fragmenty, które nie były potrzebne do mojego menu
#kod jest ten sam w menu_początkowy, menu_pausa i menu_koncowe
#wszystkie zdjecia pobrałam z https://pixelartmaker.com/, oprócz zdjecia backgroundu, które pobrałam stąd z githuba
#oraz zdjecie czarnego kwadratu, które jest w menu_pauza oraz menu_koncowe pochodzi ze strony http://profilki.pl/pliki/kursory/244-czarny-kwadrat
import pygame
import button

pygame.init()

screen_width=1500
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Main Menu")



game=False
menu_state = "main"

start_img = pygame.image.load("Button1/button_start (6).png").convert_alpha()
start_button = button.Button(550, 300, start_img, 1)
background_img=pygame.image.load("Button1/bg (1).png").convert_alpha()


run=True
while run: 
    screen.fill((1,1,20))
    screen.blit(background_img,(0,0))
    if game==True:
        pass
    if start_button.draw(screen):
        menu_state = "main"

    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game=True
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()

pygame.quit()

