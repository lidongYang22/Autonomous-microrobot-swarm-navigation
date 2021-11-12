# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:10:14 2021

@author: hitjj
"""

from PIL import Image
import math
from DQN_nn import Net
from DQN_ratio import Net_ratio
import torch
from torchvision import transforms
from draw_v2 import draw_rectangular
from draw_v2 import draw_current_rectangular
from draw_v2 import draw_current_swarm
import time

net_ratio = Net_ratio(128)
net_angle = Net(128)

resize = 512

net_ratio.load_state_dict(torch.load('./checkpoint_ratio.pth'))
net_angle.load_state_dict(torch.load('./checkpoint_angle.pth'))

net_ratio.eval()
net_angle.eval()

tra = transforms.Compose([transforms.ToTensor(), transforms.Normalize(0.5, 0.5)])

x_list = []
y_list = []

x = open('./x_v2.txt', 'r')
x_list = x.read().split('\n')[:-1]
y = open('./y_v2.txt', 'r')
y_list = y.read().split('\n')[:-1]

pic = Image.open('./channel.png')
size = pic.size

size_x = size[0]
size_y = size[1]
pic = pic.resize((int(size_x * 1), int(size_y * 1)))
pic = pic.convert('RGB')

for i in range(len(y_list)):
    x_list[i] = int(1 * int(x_list[i]))
    y_list[i] = int((size[1] - 1 - int(y_list[i])* 1))#  

tab = []
for i in range(256):
    if i < 100:
        tab.append(1)
    else:
        tab.append(0)

pic = pic.convert('L')
pic = pic.point(tab, '1')
pic = pic.convert('RGB')

for i in range(pic.size[0]):
    for j in range(pic.size[1]):
        if pic.getpixel((i, j)) == (255, 255, 255):
            pic.putpixel((i, j), (0, 255, 0))

square_length = 5

ratio = 2
angle = math.pi / 2
img_whole = Image.open('./channel.png')
img_whole = img_whole.resize((int(size_x * 1), int(size_y * 1)))
size = img_whole.size
print(size)
img_whole = img_whole.convert('L')
img_whole = img_whole.point(tab, '1')
img_whole = img_whole.convert('RGB')
for i in range(size[0]):
    for j in range(size[1]):
        if img_whole.getpixel((i,j)) == (255, 255, 255):
            img_whole.putpixel((i,j), (0, 255, 0))
        else:
            img_whole.putpixel((i,j), (0, 0, 0))

ang_diff = 15 * math.pi / 180

for i in range(1, len(x_list) - 1):
    start = time.time()
    x_top_left = max(x_list[i] - 64, 0)
    y_top_left = min(y_list[i] + 64, size[1] - 1)
    
    if x_top_left + 128 > size[0] - 1:
        x_down_right = size[0] - 1
        x_top_left = size[0] - 1 - 128
    else:
        x_down_right = x_top_left + 128
        
    if y_top_left - 128 < 0:
        y_down_right = 0
        y_top_left = y_down_right + 128
    else:
        y_down_right = y_top_left - 128
    
    x_n_top_left = max(x_list[i + 1] - 64, 0)
    y_n_top_left = min(y_list[i + 1] + 64, size[1] - 1)

    if x_n_top_left + 128 > size[0] - 1:
        x_n_down_right = size[0] - 1
        x_n_top_left = size[0] - 1 - 128
    else:
        x_n_down_right = x_n_top_left + 128
        
    if y_n_top_left - 128 < 0:
        y_n_down_right = 0
        y_n_top_left = y_n_down_right + 128
    else:
        y_n_down_right = y_n_top_left - 128
    
    if x_list[i+1] == x_list[i]:
        ang_between = math.pi / 2
    else:
        tan = (y_list[i+1] - y_list[i]) / (x_list[i+1] - x_list[i])
        ang_between = math.atan(tan)
    
    img = pic.crop((x_top_left, size[1] - 1 -y_top_left, x_down_right, size[1] - 1 - y_down_right))
    img_next = pic.crop((x_n_top_left, size[1] - 1 -y_n_top_left, x_n_down_right, size[1] - 1 - y_n_down_right))
    print(x_list[i], x_top_left, y_list[i], y_down_right)
    img1 = draw_rectangular(img, x_list[i] - x_top_left, y_list[i] - y_down_right, 350, ratio, angle, 128, 128)
    img_1 = draw_current_swarm(img1, x_list[i + 1] - x_top_left, y_list[i + 1] - y_down_right, square_length, 128, 128)
    img_1 = tra(img_1)
    img_1 = img_1.unsqueeze(0)
    
    ratio_out = net_ratio(img_1)

    i_temp = 0
    r_temp = ratio_out[0][0]
    for j in range(1, 5):
        if ratio_out[0][j] > r_temp:
            r_temp = ratio_out[0][j]
            i_temp = j
    
    ratio = i_temp + 2
    print('index:' + str(i))
    print('ratio:' +str(ratio))
    
    img_2 = draw_current_rectangular(img_next, x_list[i + 1] - x_n_top_left, y_list[i + 1] - y_n_down_right, 350, ratio, ang_between, 128, 128)
    img_2_left = draw_current_rectangular(img_next, x_list[i + 1] - x_n_top_left, y_list[i + 1] - y_n_down_right, 350, ratio, ang_between - ang_diff, 128, 128)
    img_2_right = draw_current_rectangular(img_next, x_list[i + 1] - x_n_top_left, y_list[i + 1] - y_n_down_right, 350, ratio, ang_between + ang_diff, 128, 128)
    
    tensor_2 = tra(img_2)
    tensor_2_left = tra(img_2_left)
    tensor_2_right = tra(img_2_right)
    
    tensor_total = torch.cat((tensor_2_left, tensor_2, tensor_2_right), 0)
    
    tensor_total = tensor_total.unsqueeze(0)
    angle_out = net_angle(tensor_total)

    if ratio == 1:
        angle = 0
    else:
        angle = ang_between + (float(angle_out) - 0.5) * 90 * math.pi / 180
    print('angle:' + str(float(angle_out)))
    
    end = time.time()
    print('time is:' + str(end - start) + 's')
    
    img = draw_current_rectangular(img_whole, x_list[i + 1], y_list[i + 1], 350, ratio, angle, size[0], size[1])
    img.save('./out/' + str(i) + '.png', quality = 95, subsampling = 0)
