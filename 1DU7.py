import pygame, time

pygame.init()
width, height = 800, 600
dvdLogoSpeed = [1, 1]
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))

dvdLogo = pygame.image.load("ggg")
dvdLogoRect = dvdLogo.get_rect()

while True:
    screen.fill(backgroundColor)

    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

    pygame.display.flip()
    time.sleep(10 / 1000)