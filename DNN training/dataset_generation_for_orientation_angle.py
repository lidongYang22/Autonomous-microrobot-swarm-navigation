
import os
import math
from torch.utils.data import DataLoader
import matplotlib

def maze_shuffle():

    files = os.listdir('./training_dataset_for_swarm_orientation_angle')

    file_list = DataLoader(files, shuffle = True, batch_size = 1)

    n = len(files)

    print(n)

    count_train = 0
    count_test = 0

    train = []
    test = []

    f = open('./train_dataset.txt', 'w').close()
    f = open('./test_dataset.txt', 'w').close()

    for i,name in enumerate(file_list):

        if i < math.ceil(0.9 * n):
            train.append(name[0])
            count_train = count_train + 1
        else:
            test.append(name[0])
            count_test = count_test + 1

    f = open('./train_dataset.txt', 'a')
    for i in range (count_train):
        f.write(train[i] + '\n')
    f.close()

    f = open('./test_dataset.txt', 'a')
    for i in range (count_test):
        f.write(test[i] + '\n')
    f.close()