import pygame
import sys
from Qr_code import Qrcode



my_qrcode = Qrcode(3, 'byte', "M", 0)
my_qrcode.set_up()
my_qrcode.process_massage("www.youtube.com")
listt = my_qrcode.data_list

my_list = []
for key in listt:
    my_list.append(listt.get(key))




def darw_squares(listt, size):
    for y in range(size):
        for x in range(size):
            if listt[y * size + x] == 0:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x / size * WIDTH + PADDING, y / size * HEIGHT + PADDING, WIDTH / size, HEIGHT / size))
            elif listt[y * size + x] == 1:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x / size * WIDTH + PADDING, y / size * HEIGHT + PADDING, WIDTH / size, HEIGHT / size))
            else:
                pygame.draw.rect(screen, GRAY, pygame.Rect(x / size * WIDTH + PADDING, y / size * HEIGHT + PADDING, WIDTH / size, HEIGHT / size))


pygame.init()
WIDTH, HEIGHT = 300, 300
PADDING = 50

WHITE = (255, 255, 255)
BLACK = (25, 25, 25)
GRAY = (125, 125, 125)

screen = pygame.display.set_mode((WIDTH + PADDING * 2, HEIGHT + PADDING * 2))
pygame.display.set_caption("Qr code")


screen.fill(WHITE)
darw_squares(my_list, my_qrcode.width)
pygame.display.flip()



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



pygame.quit()
sys.exit()

