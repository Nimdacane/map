import pygame

map = ['##########',
       '#..#..#..#',
       '....##....',
       '#........#',
       '##########']

yy = -1
xx = -1

pygame.init()

block = False

sc = pygame.display.set_mode((1000, 500))

while True:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill((0, 0, 0))

    for y in map:
        yy += 1
        for x in y:
            xx += 1
            if x == '#':
                pygame.draw.rect(sc, (191, 191, 191), (100 * xx, 100 * yy, 100, 100))
        xx = -1
    yy = -1

    pygame.display.update()