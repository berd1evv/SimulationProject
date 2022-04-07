from random import randint
import pygame

exit = False

size = width, height = 800, 600
bg_color = (0, 0, 0) 
fullscreen = False  


logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (100, 50))
clock = pygame.time.Clock()
img_size = logo.get_rect().size
screen = pygame.display.set_mode(size)
pygame.display.set_caption('DVD Bounce')
if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

x = randint(50, width-60)
y = randint(50, height-60)
x_speed = 3
y_speed = 3


def move(x, y):
    screen.blit(logo, (x, y))


while exit == False:
    screen.fill(bg_color)
    if (x + img_size[0] >= width) or (x <= 0):
        x_speed = -x_speed
    if (y + img_size[1] >= height) or (y <= 0):
        y_speed = -y_speed
    x += x_speed
    y += y_speed
    move(x, y)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

pygame.quit()