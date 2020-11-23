import pygame
from sklearn import svm

pygame.init()
sc = pygame.display.set_mode((1200, 800))
sc.fill((255, 255, 255))
pygame.display.update()
clock = pygame.time.Clock()
FPS = 2
flag = True
data = []
cluster = []


def addGreenPoint(i):
    data.append([i.pos[0], i.pos[1]])
    cluster.append(1)
    pygame.draw.circle(sc, (225, 0, 50), i.pos, 10)
    pygame.display.update()


def addRedPoint(i):
    data.append([i.pos[0], i.pos[1]])
    cluster.append(-1)
    pygame.draw.circle(sc, (0, 225, 0), i.pos, 10)
    pygame.display.update()


def showLines():
    model = svm.SVC(kernel='linear', C=1.0)
    model.fit(data, cluster)
    W = model.coef_[0]
    I = model.intercept_
    n = -W[0] / W[1]
    m = I[0] / W[1]
    y11 = -m
    x11 = m / n
    y12 = 1 / W[1] - m
    x22 = 1 / W[0] + m / n
    y13 = -1 / W[1] - m
    x23 = -1 / W[0] + m / n
    pygame.draw.aaline(sc, (0, 0, 0), [0, y12], [x22, 0])
    pygame.draw.aaline(sc, (0, 0, 0), [0, y13], [x23, 0])
    pygame.draw.line(sc, (0, 0, 0), [0, y11], [x11, 0], 2)
    pygame.display.update()


while flag:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            pygame.quit()
            flag = False

        if i.type == pygame.MOUSEBUTTONDOWN:

            if i.button == 1:
                addGreenPoint(i)

            if i.button == 3:
                addRedPoint(i)

        if i.type == pygame.KEYDOWN:

            if i.key == pygame.KMOD_RSHIFT:
                showLines()

    clock.tick(FPS)
