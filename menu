import pygame
import button #klasa z przyciskami 

pygame.init()
#tutaj okno gry (mysle ze po wspólnych ustaleniach)
ekran=pygame.display.set_mode()
pygame.display.set_caption("Main Menu/Menu")

gra_pauza=False
main_menu="Main Menu/Menu"
#czcionka i kolor tekstu (rowniez po wspólnych ustaleniach)
czcionka=pygame.font.()
kolor_tekstu=()
#przyciski zdjecia - na razie jeszcze nie ma
pauza_img=pygame.image.load("").convert_alpha()
ustawienia_img=pygame.image.load("").convert_alpha()
dzwiek_img=pygame.image.load("").convert_alpha()
pomoc_img=pygame.image.load("").convert_alpha()
wyjscie_img=pygame.image.load("").convert_alpha()
Arcade_img=pygame.image.load("").convert_alpha()
Versus_img=pygame.image.load("").convert_alpha()
Network_img=pygame.image.load("").convert_alpha()
Training_img=pygame.image.load("").convert_alpha()
Challenge_img=pygame.image.load("").convert_alpha()
Customize_img=pygame.image.load("").convert_alpha()
Player_Data_img=pygame.image.load("").convert_alpha()
Store_img=pygame.image.load("").convert_alpha()
powrot_img=pygame.image.load("").convert_alpha()
start_img=pygame.image.load("").convert_alpha()
#przyciski
pauza_przycisk=button.Button(344,100,pauza_img,1) #przyklad
ustawienia_przycisk=button.Button(ustawienia_img,1)
dzwiek_przycisk=button.Button(dzwiek_img,1)
pomoc_przycisk=button.Button(pomoc_img,1)
wyjscie_przycisk=button.Button(wyjscie_img,1)
Arcade_przycisk=button.Button(Arcade_img,1)
Versus_przycisk=button.Button(Versus_img,1)
Network_przycisk=button.Button(Network_img,1)
Training_przycisk=button.Button(Training_img,1)
Challenge_przycisk=button.Button(Challenge_img,1)
Customize_przycisk=button.Button(Customize_img,1)
Player_Data_przycisk=button.Button(Player_Data_img,1)
Store_przycisk=button.Button(Store_img,1)
powrot_przycisk=button.Button(powrot_img,1)
start_przycisk=button.Button(start_img,1)

#funkcje
class Menu():
    def wyswietlenie_tekstu(tekst,czcionka,kolor_tekstu,x,y):


#menu - gra
gra=True
while gra:
    if gra_pauza==True:
        if main_menu=="Main Menu/Menu":
            if pauza_przycisk.draw(ekran):
                gra_pauza=False #zeby wrocic do gry
            elif Arcade_przycisk.draw(ekran):
                main_menu=="Arcade"
            elif Versus_przycisk.draw(ekran):
                main_menu=="Versus"
            elif Network_przycisk.draw(ekran):
                main_menu=="Network"
            elif Training_przycisk.draw(ekran):
                main_menu=="Training"
            elif Challenge_przycisk.draw(ekran):
                main_menu=="Challenge"
            elif Customize_przycisk.draw(ekran):
                main_menu=="Customize"
            elif Player_Data_przycisk.draw(ekran):
                main_menu=="Player Data"
            elif ustawienia_przycisk.draw(ekran):
                main_menu=="Ustawienia/Settings"
            elif Store_przycisk.draw(ekran):
                main_menu=="Store"
            elif wyjscie_przycisk.draw(ekran):
                gra=False #wyjscie z gry
        elif main_menu=="Ustawienia/Settings":
            if dzwiek_przycisk.draw(ekran):
                print("Głośność")
            elif pomoc_przycisk.draw(ekran):
                print("Pomoc")
            elif powrot_przycisk.draw(ekran):
                main_menu="Main menu/Menu" #powrot do glownego menu
        elif main_menu=="Training":
            if start_przycisk.draw(ekran):
                print("Start")
            elif powrot_przycisk.draw(ekran):
                main_menu=="Main menu/Menu"
    else:
        wyswietlenie_tekstu("gra", czcionka, kolor_tekstu) #bedzie trwala gra
        



    #tutaj co sie bedzie działo po wciśnięciu danego przycisku
    for przycisk in pygame.przycisk.get():
        if przycisk.type==pygame.KEYDOWN:
            if przycisk.key==pygame.K_SPACE:
                gra_pauza=True


pygame.quit()
