import numpy as np

class Maze(object):

    def __init__(self, train, root):
        if train == True:
            self.root = root + './angle_output_rotate_situation/'
            f = open(root + 'train_dataset.txt', 'r')
            self.maze_names = f.read()
            self.maze_names = self.maze_names.split()
            self.train = True
        else:
            self.root = root + './angle_output_rotate_situation/'
            f = open(root + 'test_dataset.txt', 'r')
            self.maze_names = f.read()
            self.maze_names = self.maze_names.split()
            self.train = False

        self.seed_set = False

    def __len__(self):
        return len(self.maze_names)

    def get_maze_name(self):
        name_index = np.random.randint(1, len(self))
        name = self.root + self.maze_names[name_index]
        return name

    def __getitem__(self,index):
        if not self.seed_set:
            np.random.seed(index)
            self.seed_set = True
        return(self.get_maze_name())