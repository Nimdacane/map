import pygame

map = []

size = 20
mapSize = 75
mapCount = 0

with open('map.txt') as mapTXT:
    maptxt = mapTXT.read()

for Count in range(1, 39):
    map.append(maptxt[(mapSize * mapCount) + Count:(mapSize * (mapCount + 1) + Count)])
    mapCount += 1

yy = -1
xx = -1

pygame.init()

sc = pygame.display.set_mode((1500, 760))

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for y in map:
        yy += 1
        for x in y:
            xx += 1
            if x == 'A':
                pygame.draw.rect(sc, (0, 0, 127), (size * xx, size * yy, size, size))
            elif x == 'B':
                pygame.draw.rect(sc, (0, 0, 255), (size * xx, size * yy, size, size))
            elif x == 'C':
                pygame.draw.rect(sc, (0, 127, 0), (size * xx, size * yy, size, size))
            elif x == 'D':
                pygame.draw.rect(sc, (0, 127, 127), (size * xx, size * yy, size, size))
            elif x == 'E':
                pygame.draw.rect(sc, (0, 127, 255), (size * xx, size * yy, size, size))
            elif x == 'F':
                pygame.draw.rect(sc, (0, 255, 0), (size * xx, size * yy, size, size))
            elif x == 'G':
                pygame.draw.rect(sc, (0, 255, 127), (size * xx, size * yy, size, size))
            elif x == 'H':
                pygame.draw.rect(sc, (0, 255, 255), (size * xx, size * yy, size, size))
            elif x == 'I':
                pygame.draw.rect(sc, (127, 0, 0), (size * xx, size * yy, size, size))
            elif x == 'J':
                pygame.draw.rect(sc, (127, 0, 127), (size * xx, size * yy, size, size))
            elif x == 'K':
                pygame.draw.rect(sc, (127, 0, 255), (size * xx, size * yy, size, size))
            elif x == 'L':
                pygame.draw.rect(sc, (127, 127, 0), (size * xx, size * yy, size, size))
            elif x == 'M':
                pygame.draw.rect(sc, (127, 127, 127), (size * xx, size * yy, size, size))
            elif x == 'N':
                pygame.draw.rect(sc, (127, 127, 255), (size * xx, size * yy, size, size))
            elif x == 'O':
                pygame.draw.rect(sc, (127, 255, 0), (size * xx, size * yy, size, size))
            elif x == 'P':
                pygame.draw.rect(sc, (127, 255, 127), (size * xx, size * yy, size, size))
            elif x == 'Q':
                pygame.draw.rect(sc, (127, 255, 255), (size * xx, size * yy, size, size))
            elif x == 'R':
                pygame.draw.rect(sc, (255, 0, 0), (size * xx, size * yy, size, size))
            elif x == 'S':
                pygame.draw.rect(sc, (255, 0, 127), (size * xx, size * yy, size, size))
            elif x == 'T':
                pygame.draw.rect(sc, (255, 0, 255), (size * xx, size * yy, size, size))
            elif x == 'U':
                pygame.draw.rect(sc, (255, 127, 0), (size * xx, size * yy, size, size))
            elif x == 'V':
                pygame.draw.rect(sc, (255, 127, 127), (size * xx, size * yy, size, size))
            elif x == 'W':
                pygame.draw.rect(sc, (255, 127, 255), (size * xx, size * yy, size, size))
            elif x == 'X':
                pygame.draw.rect(sc, (255, 255, 0), (size * xx, size * yy, size, size))
            elif x == 'Y':
                pygame.draw.rect(sc, (255, 255, 127), (size * xx, size * yy, size, size))
            elif x == 'Z':
                pygame.draw.rect(sc, (255, 255, 255), (size * xx, size * yy, size, size))
        xx = -1
    yy = -1

    pygame.display.update()
