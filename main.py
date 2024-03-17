import pygame
import math
import random
import time

#presets
#----------------------------------------------------
array_of_cubes = False
single_cube = False
#----------------------------------------------------


t1 = time.time()

quadrantLen = 500

win = pygame.display.set_mode((quadrantLen * 2, quadrantLen * 2))  # window size
pygame.display.set_caption("pygame")  # defines the windows name


class Cuboid:
    def __init__(self, pos=[10, 10, 10], radius=2, angle=math.pi / 4):
        self.pos = pos
        self.radius = radius
        self.adjustedRadius = radius * math.sqrt(2)
        self.points = {}
        self.angle = angle
        self.colors = (
            (0, 0, 255),
            (255, 0, 0),
            (0, 255, 0),
            (255, 128, 0),
            (255, 255, 0),
            (255, 255, 255)
        )
        print('hello')

    def find_points(self):
        self.points = (
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi), self.pos[2] + self.radius],
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi), self.pos[2] - self.radius],
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 1.5),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 1.5), self.pos[2] + self.radius],
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 1.5),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 1.5), self.pos[2] - self.radius],

            [self.pos[0] + self.adjustedRadius * math.cos(self.angle),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle), self.pos[2] + self.radius],
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle), self.pos[2] - self.radius],
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 0.5),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 0.5), self.pos[2] + self.radius],
            [self.pos[0] + self.adjustedRadius * math.cos(self.angle + math.pi * 0.5),
             self.pos[1] + self.adjustedRadius * math.sin(self.angle + math.pi * 0.5), self.pos[2] - self.radius]
        )

    def find_side_positions(self):
        self.sidesOrder = {}
        for indx, side in enumerate(self.cuboidSides):
            distance = abs(self.points[side[0]][0] + self.points[side[3]][0]) + self.points[side[0]][1] + \
                       self.points[side[3]][1]
            self.sidesOrder[indx] = distance
        self.sidesOrder = list(dict(sorted(self.sidesOrder.items(), key=lambda item: item[1], reverse=True)).keys())


    def find_2d_position(self, point):
        return (quadrantLen + math.degrees(math.atan(self.points[point][0] / self.points[point][1])) * 15,
                quadrantLen - math.degrees(math.atan(self.points[point][2] / self.points[point][1])) * 15)

    def draw_points(self):
        for pIndex in range(len(self.points)):
            pygame.draw.circle(win, (255, 255, 255),
                               (500 + math.degrees(math.atan(self.points[pIndex][0] / self.points[pIndex][1])) * 15,
                                500 - math.degrees(math.atan(self.points[pIndex][2] / self.points[pIndex][1])) * 15), 3)

    rectangleEdges = (
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

    def draw_lines(self):
        for edge in self.rectangleEdges:
            pygame.draw.line(win, (255, 255, 255),
                             self.find_2d_position(edge[0]),
                             self.find_2d_position(edge[1]))

    cuboidSides = (
        (0, 1, 3, 2),
        (2, 3, 5, 4),
        (4, 5, 7, 6),
        (6, 7, 1, 0)
    )
    def draw_sides(self):



        for side in self.sidesOrder:
            pygame.draw.polygon(win, self.colors[side], (
                self.find_2d_position(self.cuboidSides[side][0]),
                self.find_2d_position(self.cuboidSides[side][1]),
                self.find_2d_position(self.cuboidSides[side][2]),
                self.find_2d_position(self.cuboidSides[side][3])))

        if self.pos[2] > self.radius:
            pygame.draw.polygon(win, self.colors[5], (
                self.find_2d_position(1),
                self.find_2d_position(3),
                self.find_2d_position(5),
                self.find_2d_position(7)))
        elif self.pos[2] < -self.radius:
            pygame.draw.polygon(win, self.colors[4], (
                self.find_2d_position(0),
                self.find_2d_position(2),
                self.find_2d_position(4),
                self.find_2d_position(6)))



        #pygame.draw.circle(win, (255, 0, 0), self.find_2d_position(2), 3)


    def move(self, dir):
        self.find_points()
        self.find_side_positions()
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


c1 = Cuboid([5, 15, 5], 1)
c2 = Cuboid([5, 15, 5], 1)

cubes = {}
if single_cube:
    cubes[int(len(cubes))] = Cuboid([5, 15, 5], 2)
# cubes[int(len(cubes))] = Cuboid([5, 15, 5], 1)

if array_of_cubes:
    for j in range(10):
        for i in range(10):
            cubes[int(len(cubes))] = Cuboid([j*2 - 10, 15, i*2 - 10], 0.5)

cubes1 = {}
cubes2 = {}
cubes3 = {}
cubes4 = {}

for i in range(10):
    cubes1[int(len(cubes1))] = Cuboid([5, 15, 5], 1)

for i in range(10):
    cubes2[int(len(cubes2))] = Cuboid([5, 15, 5], 1)

for i in range(10):
    cubes3[int(len(cubes3))] = Cuboid([5, 15, 5], 1)

for i in range(10):
    cubes4[int(len(cubes4))] = Cuboid([5, 15, 5], 1)

for index in cubes1:
    cubes1[index].find_points()
    cubes1[index].find_side_positions()
    cubes2[index].find_points()
    cubes2[index].find_side_positions()
    cubes3[index].find_points()
    cubes3[index].find_side_positions()

cubes1[0].colors = ((250, 20, 20), (150, 50, 50), (250, 20, 20), (150, 50, 50), (255, 0, 0), (100, 0, 0))
cubes1[1].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes1[2].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes1[3].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes1[4].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))
cubes1[5].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes1[6].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes1[7].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes1[8].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes1[9].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))

cubes2[0].colors = ((250, 20, 20), (150, 50, 50), (250, 20, 20), (150, 50, 50), (255, 0, 0), (100, 0, 0))
cubes2[1].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes2[2].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes2[3].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes2[4].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))
cubes2[5].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes2[6].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes2[7].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes2[8].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes2[9].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))

cubes3[0].colors = ((250, 20, 20), (150, 50, 50), (250, 20, 20), (150, 50, 50), (255, 0, 0), (100, 0, 0))
cubes3[1].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes3[2].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes3[3].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes3[4].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))
cubes3[5].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes3[6].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes3[7].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes3[8].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes3[9].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))

cubes4[0].colors = ((250, 20, 20), (150, 50, 50), (250, 20, 20), (150, 50, 50), (255, 0, 0), (100, 0, 0))
cubes4[1].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes4[2].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes4[3].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes4[4].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))
cubes4[5].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes4[6].colors = ((250, 250, 250), (240, 240, 240), (250, 250, 250), (240, 240, 240),  (255, 255, 255), (200, 200, 200))
cubes4[7].colors = ((20, 250, 20), (50, 150, 50), (20, 250, 20), (50, 150, 50), (0, 255, 0), (0, 100, 0))
cubes4[8].colors = ((20, 20, 250), (50, 50, 150), (20, 20, 250), (50, 50, 150), (0, 0, 255), (0, 0, 100))
cubes4[9].colors = ((200, 200, 0), (170, 170, 0), (200, 200, 0), (170, 170, 0), (255, 255, 0), (150, 150, 0))

slowdownTrigger = [False, False, False, False]
speed = [12, 12, 12, 12]
pos = [0, 0, 0, 0]
x = 0

y = random.randint(0, 9)

running = True
while running:
    pygame.time.delay(20)  # time between frames (in ms)
    for event in pygame.event.get():  # when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # all pressed keys

    win.fill((0, 0, 0))  # fills screen background

    pygame.draw.circle(win, (255, 0, 0), (500, 500), 3)



    if pos[0] % 360 == y * 36:
        pos[0] += 6
        slowdownTrigger[0] = True

    if pos[1] % 360 == (180 + y * 36) % 360:
        pos[1] += 6
        slowdownTrigger[1] = True

    if pos[2] % 360 == (240 + y * 36) % 360:
        pos[2] += 6
        slowdownTrigger[2] = True

    if pos[3] % 360 == y * 36:
        pos[3] += 6
        slowdownTrigger[3] = True


    if slowdownTrigger[0]:
        speed[0] -= 0.1
    if slowdownTrigger[1]:
        speed[1] -= 0.08
    if slowdownTrigger[2]:
        speed[2] -= 0.06
    if slowdownTrigger[3]:
        speed[3] -= 0.04

    if speed[0] > 0: pos[0] += speed[0]
    if speed[1] > 0: pos[1] += speed[1]
    if speed[2] > 0: pos[2] += speed[2]
    if speed[3] > 0: pos[3] += speed[3]


    x += 1
    print(x)
    if x == 10000:
        print(time.time()-t1)
        pass

    if keys[pygame.K_a]:
        slowdownTrigger[0] = True
        for index in cubes1:
            cubes1[index].move(0)

    if keys[pygame.K_d]:
        slowdownTrigger[1] = True
        for index in cubes1:
            cubes1[index].move(1)

    if keys[pygame.K_s]:
        slowdownTrigger[2] = True
        for index in cubes1:
            cubes1[index].move(2)

    if keys[pygame.K_w]:
        slowdownTrigger[3] = True
        for index in cubes1:
            cubes1[index].move(3)

    if keys[pygame.K_j]:
        for index in cubes1:
            cubes1[index].move(4)

    if keys[pygame.K_k]:
        for index in cubes1:
            cubes1[index].move(5)

    if keys[pygame.K_f]:
        for index in cubes1:
            cubes1[index].move(6)

    #rwbgybwgby
    
    


    cubes1 = dict(sorted(cubes1.items(), key=lambda item: item[1].pos[1], reverse=True))

    for indx in cubes1:
        cubes1[indx].pos = [-4.5, math.cos(indx * math.pi/5 + pos[0] * 0.0174533)*5+15, math.sin(indx * math.pi/5 + pos[0] * 0.0174533)*5]
        cubes1[indx].find_points()
        cubes1[indx].find_side_positions()
        cubes1[indx].draw_sides()
        #cubes[index].move(6)

    cubes4 = dict(sorted(cubes4.items(), key=lambda item: item[1].pos[1], reverse=True))

    for indx in cubes4:
        cubes4[indx].pos = [4.5, math.cos(indx * math.pi/5 + pos[3] * 0.0174533)*5+15, math.sin(indx * math.pi/5 + pos[3] * 0.0174533)*5]
        cubes4[indx].find_points()
        cubes4[indx].find_side_positions()
        cubes4[indx].draw_sides()
        #cubes[index].move(6)
    
    cubes2 = dict(sorted(cubes2.items(), key=lambda item: item[1].pos[1], reverse=True))

    for indx in cubes2:
        cubes2[indx].pos = [-1.5, math.cos(indx * math.pi/5 + pos[1] * 0.0174533)*5+15, math.sin(indx * math.pi/5 + pos[1] * 0.0174533)*5]
        cubes2[indx].find_points()
        cubes2[indx].find_side_positions()
        cubes2[indx].draw_sides()
        #cubes[index].move(6)
    
    cubes3 = dict(sorted(cubes3.items(), key=lambda item: item[1].pos[1], reverse=True))

    for indx in cubes3:
        cubes3[indx].pos = [1.5, math.cos(indx * math.pi/5 + pos[2] * 0.0174533)*5+15, math.sin(indx * math.pi/5 + pos[2] * 0.0174533)*5]
        cubes3[indx].find_points()
        cubes3[indx].find_side_positions()
        cubes3[indx].draw_sides()
        #cubes[index].move(6)
    
 #

    pygame.display.update()
pygame.quit()  # when the loop ends it closes the window
