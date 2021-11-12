import torch
from PIL import Image
import math
import copy

threshold = 100
tab = []
for i in range(256):
    if i < threshold:
        tab.append(0)
    else:
        tab.append(1)

def draw_rectangular(pic, c_x, c_y, area, ratio, angle, resize_x, resize_y):

    maze = copy.deepcopy(pic)

    short_side = math.sqrt(area / ratio) / 2
    long_side = short_side * ratio

    diagnoal = math.sqrt(short_side**2 + long_side**2)
    short_side = short_side
    long_side = long_side
    diagnoal = diagnoal

    for i in range(int(c_x - diagnoal), int(c_x + diagnoal + 1)):
        for j in range(int(c_y - diagnoal), int(c_y + diagnoal + 1)):
            if i == c_x:
                if j == c_y:
                    maze.putpixel((i, resize_y - 1 - j), (maze.getpixel((i, resize_y - 1 - j))[0], maze.getpixel((i, resize_y - 1 - j))[1], 255))
                    continue
                elif j > c_y:
                    tan = math.pi / 2
                elif j < c_y:
                    tan = -math.pi / 2
            else:
                tan = (c_y - j) / (c_x - i)
                tan = math.atan(tan)

            tan = tan - angle
            diag_current = math.sqrt((i - c_x)**2 + (j - c_y)**2)
            x_current = math.fabs(diag_current * math.cos(tan))
            y_current = math.fabs(diag_current * math.sin(tan))
            if x_current < long_side and y_current < short_side:

                maze.putpixel((i, resize_y - 1 - j), (maze.getpixel((i, resize_y - 1 - j))[0], maze.getpixel((i, resize_y - 1 - j))[1], 255))

    return maze

def draw_current_rectangular(pic, c_x, c_y, area, ratio, angle, resize_x, resize_y):

    maze = copy.deepcopy(pic)

    short_side = math.sqrt(area / ratio) / 2
    long_side = short_side * ratio

    diagnoal = math.sqrt(short_side**2 + long_side**2)
    short_side = short_side
    long_side = long_side
    diagnoal = diagnoal

    for i in range(int(c_x - diagnoal), int(c_x + diagnoal + 1)):
        for j in range(int(c_y - diagnoal), int(c_y + diagnoal + 1)):
            if i == c_x:
                if j == c_y:
                    maze.putpixel((i, resize_y - 1 - j), (255, maze.getpixel((i, resize_y - 1 - j))[1], maze.getpixel((i, resize_y - 1 - j))[2]))
                    continue
                elif j > c_y:
                    tan = math.pi / 2
                elif j < c_y:
                    tan = -math.pi / 2
            else:
                tan = (c_y - j) / (c_x - i)
                tan = math.atan(tan)

            tan = tan - angle
            diag_current = math.sqrt((i - c_x)**2 + (j - c_y)**2)
            x_current = math.fabs(diag_current * math.cos(tan))
            y_current = math.fabs(diag_current * math.sin(tan))
            if x_current < long_side and y_current < short_side:
                maze.putpixel((i, resize_y - 1 - j), (255, maze.getpixel((i, resize_y - 1 - j))[1], maze.getpixel((i, resize_y - 1 - j))[2]))
    return maze

def draw_swarm(pic, c_x, c_y, area, ratio, angle, resize_x, resize_y):

    maze = copy.deepcopy(pic)

    if ratio == 1:
        ratio = 1

    r_long = math.sqrt(area * ratio / math.pi)
    r_short = r_long / ratio
    focal_length = math.sqrt(math.pow(r_long, 2) - math.pow(r_short, 2))

    focus1_x = c_x - focal_length*math.cos(angle)
    focus1_y = c_y - focal_length*math.sin(angle)
    focus2_x = c_x + focal_length*math.cos(angle)
    focus2_y = c_y + focal_length*math.sin(angle)

    for i in range(max(0,(int(c_x - r_long) - 1)),min(resize_x,(int(c_x + r_long) + 2))):
        for j in range(max(0, (int(c_y - r_long) - 1)), min(resize_y, (int(c_y + r_long) + 2))):
            if (math.sqrt(math.pow(i-focus1_x, 2) + math.pow(j-focus1_y, 2)) + math.sqrt(math.pow(i-focus2_x, 2) + math.pow(j-focus2_y, 2))) <= r_long * 2:
                maze.putpixel((i, resize_y - 1 - j), (maze.getpixel((i, resize_y - 1 - j))[0], maze.getpixel((i, resize_y - 1 - j))[1], 255))

    return maze

def draw_end_swarm(pic, c_x, c_y, resize_x, resize_y):
    maze = copy.deepcopy(pic)
    area = 50 #150 * math.pi
    radius = math.sqrt(area / math.pi)
    for i in range(max(0, (int(c_x - radius) - 1)), min(resize_x, (int(c_x + radius) + 2))):
        for j in range(max(0, (int(c_y - radius) - 1)), min(resize_y, (int(c_y + radius) + 2))):
            if (math.sqrt(math.pow(i - c_x, 2) + math.pow(j - c_y, 2))) <= radius:
                maze.putpixel((i, resize_y - 1 - j), (255, maze.getpixel((i,resize_y - 1 - j))[1], maze.getpixel((i,resize_y - 1 - j))[2]))
    return maze

def draw_current_swarm(pic, c_x, c_y, square_length, resize_x, resize_y):
    maze = copy.deepcopy(pic)
    for i in range(c_x - square_length, c_x + square_length + 1):
        for j in range(c_y - square_length, c_y + square_length + 1):
            maze.putpixel((i, resize_y - 1 - j),(255, maze.getpixel((i,resize_y - 1 - j))[1],  maze.getpixel((i,resize_y - 1 - j))[2]))
    return maze

def draw_next_swarm(pic, c_x, c_y, square_length, resize):
    maze = copy.deepcopy(pic)
    for i in range(c_x - square_length, c_x + square_length + 1):
        for j in range(c_y - square_length, c_y + square_length + 1):
            maze.putpixel((i, resize - 1 - j),
                          (maze.getpixel((i, resize - 1 - j))[0], 255, maze.getpixel((i, resize - 1 - j))[2]))
    return maze

def draw_current_swarm_output(pic, c_x, c_y, area, ratio, angle, resize):

    maze = copy.deepcopy(pic)

    if ratio == 1:
        ratio = 1

    r_long = math.sqrt(area * ratio / math.pi)
    r_short = r_long / ratio
    focal_length = math.sqrt(math.pow(r_long, 2) - math.pow(r_short, 2))

    focus1_x = c_x - focal_length*math.cos(angle)
    focus1_y = c_y - focal_length*math.sin(angle)
    focus2_x = c_x + focal_length*math.cos(angle)
    focus2_y = c_y + focal_length*math.sin(angle)

    for i in range(max(0,(int(c_x - r_long) - 1)),min(resize,(int(c_x + r_long) + 2))):
        for j in range(max(0, (int(c_y - r_long) - 1)), min(resize, (int(c_y + r_long) + 2))):
            if (math.sqrt(math.pow(i-focus1_x, 2) + math.pow(j-focus1_y, 2)) + math.sqrt(math.pow(i-focus2_x, 2) + math.pow(j-focus2_y, 2))) <= r_long * 2:
                maze.putpixel((i, resize - 1 - j), (255, maze.getpixel((i,resize - 1 - j))[1],  maze.getpixel((i,resize - 1 - j))[2]))

    return maze
