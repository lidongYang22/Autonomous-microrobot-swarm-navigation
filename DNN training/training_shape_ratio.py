from torch.utils.data import DataLoader
from data_load_for_shape_ratio import Maze
from DQN_ratio import Net_ratio
import torch
import torch.nn as nn
from dataset_generation_for_shape_ratio import maze_shuffle


maze_shuffle()

train_list = Maze(train=True, root='./')

maze_resize = 128

def ratio_label_generator(ratio):
    label = ratio - 2
    return(label)

is_support = torch.cuda.is_available()

if is_support:
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')

ratio_net = Net_ratio(maze_resize)
ratio_net.to(device)

ratio_net.train()


criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(ratio_net.parameters(), lr = 5e-5, momentum = 0.9)

step_count = 0 #

back_count = 0

success_maze = 0

loss_record = 0

for epoch in range(100):

    train_dataset = DataLoader(train_list.maze_names, shuffle=True, batch_size=20, num_workers=0)

    for i, dir in enumerate(train_dataset):

        first_tensor = True
        maze_batch = torch.ones(1)
        label_list = []

        for name in dir:
            maze_tensor = torch.load('./training_dataset_for_swarm_shape_ratio/' + name)
            maze_tensor = maze_tensor.unsqueeze(0)
            ratio = name.split('_')[2]
            label = ratio_label_generator(int(ratio))
            label_list.append(label)
            if first_tensor:
                first_tensor = False
                maze_batch = maze_tensor
            else:
                maze_batch = torch.cat((maze_batch, maze_tensor), 0)

        label_batch = torch.tensor(label_list)
        maze_batch = maze_batch.to(device)
        label_batch = label_batch.to(device)

        optimizer.zero_grad()
        output = ratio_net(maze_batch)

        loss = criterion(output, label_batch)

        loss.backward()
        optimizer.step()

        f = open('./loss_ratio.txt', 'a')
        f.write(str(loss.item()) + '\n' )
        f.close()

        print('epoch' + str(epoch) + 'batch' + str(i) + '，loss is' + str(loss.item()))

    checkpoint = ratio_net.state_dict()
    torch.save(checkpoint, './checkpoints_ratio/checkpoint_' + str(epoch) + '.pth')