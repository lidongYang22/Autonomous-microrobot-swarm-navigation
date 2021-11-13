from torch.utils.data import DataLoader
from data_load_for_orientation_angle import Maze
from dataset_generation_for_orientation_angle import maze_shuffle
from DQN_nn import Net
import torch
import torch.nn.functional as F

maze_shuffle()
# generate the dataset for angle training
train_list = Maze(train=True, root='./')

maze_resize = 128

# define device if GPU exists
is_support = torch.cuda.is_available()

if is_support:
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')

angle_net = Net(maze_resize)
angle_net.to(device)
angle_net.train()


optimizer = torch.optim.SGD(angle_net.parameters(), lr = 5e-5, momentum = 0.9)

loss_record = 0

for epoch in range(300):

    train_dataset = DataLoader(train_list.maze_names, shuffle=True, batch_size=20, num_workers=0)

    for i, dir in enumerate(train_dataset):
        first_tensor = True
        maze_batch = torch.ones(1)
        label_list = []

        for name in dir:
            maze_tensor = torch.load('./training_dataset_for_swarm_orientation_angle/' + name)
            maze_tensor = maze_tensor.unsqueeze(0)
            angle = name.split('_')[3]
            label = int(angle) / 90 + 0.5
            label_list.append([label])
            if first_tensor:
                first_tensor = False
                maze_batch = maze_tensor
            else:
                maze_batch = torch.cat((maze_batch, maze_tensor), 0)

        label_batch = torch.tensor(label_list)
        maze_batch = maze_batch.to(device)
        label_batch = label_batch.to(device)

        optimizer.zero_grad()
        output = angle_net(maze_batch)

        loss = F.mse_loss(output, label_batch)

        loss.backward()
        optimizer.step()

        f = open('./loss_angle.txt', 'a')
        f.write(str(loss.item()) + '\n' )
        f.close()

        print('epoch' + str(epoch) + 'batch' + str(i) + '，loss is' + str(loss.item()))

    checkpoint = angle_net.state_dict()
    torch.save(checkpoint, './checkpoints_angle/checkpoint_' + str(epoch) + '.pth')