import pygame
import math
import random

quadrantLen = 500

win = pygame.display.set_mode((quadrantLen * 2, quadrantLen * 2)) #window size
pygame.display.set_caption("pygame") #defines the windows name






class Cuboid():
    def __init__(self, pos = [10, 10, 10], radius = 2, angle = math.pi/4):
        self.pos = pos
        self.radius = radius
        self.adjustedRadius = radius*math.sqrt(2)
        self.points = {}
        self.angle = angle

    def findPoints(self):
        self.points = (
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi), self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi), self.pos[2] + self.radius],
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi), self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi), self.pos[2] - self.radius],
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 1.5), self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 1.5), self.pos[2] + self.radius],
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 1.5), self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 1.5), self.pos[2] - self.radius],

        [self.pos[0] + self.adjustedRadius * math.cos(self.angle), self.pos[1] + self.adjustedRadius * math.sin(self.angle), self.pos[2] + self.radius],
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle), self.pos[1] + self.adjustedRadius * math.sin(self.angle), self.pos[2] - self.radius],
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 0.5), self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 0.5), self.pos[2] + self.radius],
        [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 0.5), self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 0.5), self.pos[2] - self.radius]
        )
        
    def drawPoints(self):
        for index in range(len(self.points)):
            pygame.draw.circle(win, (255, 255, 255),
                               (500 + math.degrees(math.atan(self.points[index][0]/self.points[index][1])) * 15, 500 - math.degrees(math.atan(self.points[index][2]/self.points[index][1])) * 15), 3)
    rectangle_edges = (
            (0, 2),
            (2, 4),
            (4, 6),
            (6, 0),
            (1, 3),
            (3, 5),
            (5, 7),
            (7, 1),
            (0, 1),
            (2, 3),
            (4, 5),
            (6, 7),
        )
    
    def drawLines(self):

        
        for edge in self.rectangle_edges:
            pygame.draw.line(win, (255, 255, 255),
                             (quadrantLen + math.degrees(math.atan(self.points[edge[0]][0] / self.points[edge[0]][1])) * 15,
                              quadrantLen - math.degrees(math.atan(self.points[edge[0]][2] / self.points[edge[0]][1])) * 15),
                             (quadrantLen + math.degrees(math.atan(self.points[edge[1]][0] / self.points[edge[1]][1])) * 15,
                              quadrantLen - math.degrees(math.atan(self.points[edge[1]][2] / self.points[edge[1]][1])) * 15))
    cuboidSides = (
        (0, 1, 3, 2),
        (0, 2, 4, 6)
    )
    def drawSides(self):
        for side in self.cuboidSides:
            pygame.draw.polygon(win, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 

                             (
                             (quadrantLen + math.degrees(math.atan(self.points[side[0]][0] / self.points[side[0]][1])) * 15,
                              quadrantLen - math.degrees(math.atan(self.points[side[0]][2] / self.points[side[0]][1])) * 15),
                             (quadrantLen + math.degrees(math.atan(self.points[side[1]][0] / self.points[side[1]][1])) * 15,
                              quadrantLen - math.degrees(math.atan(self.points[side[1]][2] / self.points[side[1]][1])) * 15),
                             (quadrantLen + math.degrees(math.atan(self.points[side[2]][0] / self.points[side[2]][1])) * 15,
                              quadrantLen - math.degrees(math.atan(self.points[side[2]][2] / self.points[side[2]][1])) * 15),
                             (quadrantLen + math.degrees(math.atan(self.points[side[3]][0] / self.points[side[3]][1])) * 15,
                              quadrantLen - math.degrees(math.atan(self.points[side[3]][2] / self.points[side[3]][1])) * 15)))
            '''
        pygame.draw.circle(win, (255, 0, 0),
                         (quadrantLen + math.degrees(math.atan(self.points[0][0] / self.points[0][1])) * 15,
                          quadrantLen - math.degrees(math.atan(self.points[0][2] / self.points[0][1])) * 15), 0,
                          width = 10)
                          '''

    def move(self, dir):
        self.findPoints()
        if dir == 0:
            self.pos[0] -= 0.1
        if dir == 1:
            self.pos[0] += 0.1
        if dir == 2:
            self.pos[2] -= 0.1
        if dir == 3:
            self.pos[2] += 0.1
        if dir == 4:
            self.pos[1] -= 0.1
        if dir == 5:
            self.pos[1] += 0.1
        if dir == 6:
            self.angle += 0.1



#c1 = Cuboid([5, 15, 5], 2)
#c2 = Cuboid([5, 15, 5], 1)

cubes = {}
#cubes[int(len(cubes))] = Cuboid([5, 15, 5], 2)
#cubes[int(len(cubes))] = Cuboid([5, 15, 5], 1)

#'''
for j in range(10):
    for i in range(10):
        cubes[int(len(cubes))] = Cuboid([j*2 - 10, 15, i*2 - 10], 0.5)
#'''

for index in cubes:
        cubes[index].findPoints()


x = 0
running = True
while running:
    pygame.time.delay(20) #time between frames (in ms)
    for event in pygame.event.get(): #when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() #all pressed keys

    win.fill((0, 0, 0)) #fills screen background

    pygame.draw.circle(win, (255, 0, 0), (500, 500), 3)

    x += 1
    print(x)

    if keys[pygame.K_a]:
        for index in cubes:
            cubes[index].move(0)

    if keys[pygame.K_d]:
        for index in cubes:
            cubes[index].move(1)

    if keys[pygame.K_s]:
        for index in cubes:
            cubes[index].move(2)

    if keys[pygame.K_w]:
        for index in cubes:
            cubes[index].move(3)

    if keys[pygame.K_j]:
        for index in cubes:
            cubes[index].move(4)

    if keys[pygame.K_k]:
        for index in cubes:
            cubes[index].move(5)

    if keys[pygame.K_f]:
        for index in cubes:
            cubes[index].move(6)

    for index in cubes:
        #cubes[index].findPoints()
        cubes[index].drawPoints()
        cubes[index].drawLines()
        cubes[index].drawSides()




    pygame.display.update()
pygame.quit() #when the loop ends it closes the window
