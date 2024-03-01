import pygame
import math
import random
import time

#presets
#----------------------------------------------------
array_of_cubes = False
single_cube = True
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


# c1 = Cuboid([5, 15, 5], 2)
# c2 = Cuboid([5, 15, 5], 1)

cubes = {}
if single_cube:
    cubes[int(len(cubes))] = Cuboid([5, 15, 5], 2)
# cubes[int(len(cubes))] = Cuboid([5, 15, 5], 1)

if array_of_cubes:
    for j in range(10):
        for i in range(10):
            cubes[int(len(cubes))] = Cuboid([j*2 - 10, 15, i*2 - 10], 0.5)


for index in cubes:
    cubes[index].find_points()
    cubes[index].find_side_positions()

x = 0
running = True
while running:
    pygame.time.delay(20)  # time between frames (in ms)
    for event in pygame.event.get():  # when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # all pressed keys

    win.fill((0, 0, 0))  # fills screen background

    pygame.draw.circle(win, (255, 0, 0), (500, 500), 3)

    x += 1
    #print(x)
    if x == 10000:
        print(time.time()-t1)
        pass

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
        # cubes[index].findPoints()
        #cubes[index].draw_points()
        #cubes[index].draw_lines()
        cubes[index].draw_sides()

    pygame.display.update()
pygame.quit()  # when the loop ends it closes the window
