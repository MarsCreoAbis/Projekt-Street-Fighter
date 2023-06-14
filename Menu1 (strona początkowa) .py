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
