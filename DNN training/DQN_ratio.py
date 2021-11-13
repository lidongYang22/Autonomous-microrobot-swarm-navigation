import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import numpy as np
import math

is_support = torch.cuda.is_available()

if is_support:
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')

class Net_ratio(nn.Module):
    def __init__(self, size):
        super(Net_ratio,self).__init__()

        conv1_out = 32
        kernel_1 = 5
        pool = 2
        pool_stride = 2
        conv2_out = 64
        kernel_2 = 5
        conv3_out = 128
        kernel_3 = 4
        conv4_out = 128
        kernel_4 = 4
        linear_size_1 = int(conv4_out * ((((((128 - kernel_1 + 1) / 2 - kernel_2 + 1) / 2 - kernel_3 + 1) / 2 - kernel_4 + 1) / 2) ** 2))
        linear_size_2 = 650
        linear_out_size = 5

        self.conv1 = nn.Conv2d(3, conv1_out, kernel_1, padding = 0, stride = 1)
        self.bn1 = nn.BatchNorm2d(conv1_out, affine = True)
        self.pool = nn.MaxPool2d(pool, stride = pool_stride)
        self.conv2 = nn.Conv2d(conv1_out, conv2_out, kernel_2, padding = 0, stride = 1)
        self.bn2 = nn.BatchNorm2d(conv2_out, affine = True)
        self.conv3 = nn.Conv2d(conv2_out, conv3_out, kernel_3, padding = 0, stride = 1)
        self.bn3 = nn.BatchNorm2d(conv3_out, affine = True)
        self.conv4 = nn.Conv2d(conv3_out, conv4_out, kernel_4, padding = 0, stride = 1)
        self.bn4 = nn.BatchNorm2d(conv4_out, affine = True)
        self.fc1 = nn.Linear(linear_size_1, linear_size_2)
        self.fc2 = nn.Linear(linear_size_2, linear_out_size)

    def forward(self, x):
        x = self.pool(F.relu(self.bn1(self.conv1(x)))) 
        x = self.pool(F.relu(self.bn2(self.conv2(x)))) 
        x = self.pool(F.relu(self.bn3(self.conv3(x)))) 
        x = self.pool(F.relu(self.bn4(self.conv4(x)))) 
        x = x.view(-1, 128 * 5 * 5) 
        x = F.relu(self.fc1(x)) 
        x = self.fc2(x) 
        return x