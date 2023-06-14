import pygame
import button

pygame.init()

screen_width=1500
screen_height=800

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PAUSE")



game=False
menu_state = "menu2"

tlo_img = pygame.image.load("Button1/czarny_kwadrat (3) 2.jpg").convert_alpha()
tlo=button.Button(460, 120, tlo_img, 1)
background_img=pygame.image.load("Button1/BG2.JPEG").convert_alpha()
quit_img = pygame.image.load("Button1/5397d2da22b328d (1).png").convert_alpha()
quit_button=button.Button(610, 500, quit_img, 1)
replay_img = pygame.image.load("Button1/replay (1).png").convert_alpha()
replay_button=button.Button(580, 350, replay_img, 1)
stop_img = pygame.image.load("Button1/stop (5).png").convert_alpha()
stop_button=button.Button(610, 200, stop_img, 1)

run=True
while run: 
    screen.fill((1,1,20))
    screen.blit(background_img,(0,0))
    if game==True:
        pass
    if tlo.draw(screen):
        menu_state = "menu2"
    elif quit_button.draw(screen):
        menu_state="menu2"
    elif replay_button.draw(screen):
        menu_state="menu2"
    elif stop_button.draw(screen):
        menu_state="menu2"


    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game=True
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()

pygame.quit()
