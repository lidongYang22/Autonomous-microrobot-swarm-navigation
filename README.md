# Autonomous microrobot swarm navigation enabled by DL-based real-time distribution planning
This repository provides information for implementing the deep learning (DL)-based method for real-time microrobot swarm distribution planning and the method for real-time trajectory planning, both applicable for unstructured environments.

Sample codes includes:
* Training the two DNNs for swarm distribution planning
* Demonstration of the distribution planning in a channel environment
* Demonstration of the trajectory planning in a channel environment

## Table of contents
1. [Software requirement](##Softwarerequirement)
2. [Dataset](##Dataset)
3. [Sample codes and demonstrations](##Samplecodesanddemonstrations)


## Software requirement

### To run the DNN traning and distribution planning demo programes, the following softwares are needed:
* Python (version 3.6 and above)  
* numpy
* Pytorch

### To run the trajectory planning demo program, the following softwares are needed:
* Matlab (version 2016 and above)  

## Dataset
The dataset (~20 GB) used to train the two DNNs with extensive environment morphologies can be downloaded from:

[Training dataset for the swarm shape planning and the swarm orientation planning](https://mycuhk-my.sharepoint.com/:f:/g/personal/1155135830_link_cuhk_edu_hk/Er6k3hDr0hJIlXuB8HYu6L8Bs8NTN5_xK_-cJUo7VxhjCg?e=Qo8H8v)

## Sample codes and demonstrations

### DNN training
Instructions:
1. Download the codes, and the training programs for the swarm shape planning and swarm orientation planning are in './DNN training' folder.
2. Download the dataset and unzip it to the './DNN training' folder.
3. Run './DNN training/training_orientation_angle.py' and './DNN training/training_shape_ratio.py' for the swarm shape planning and swarm orientation planning, respectively.
4. Outputs: the parameters for the trained networks after each epoch will be saved in './DNN training/checkpoints_ratio' and './DNN training/checkpoints_angle' folders.

### Demo of swarm distribution planning
Instructions:
1. Download the codes, and the demo program are in './demo of ' folder.
2. Download the dataset and unzip it to the './DNN training' folder.
3. Run './DNN training/training_orientation_angle.py' and './DNN training/training_shape_ratio.py' for the swarm shape planning and swarm orientation planning, respectively.
4. Outputs: the parameters for the trained networks after each epoch will be saved in './DNN training/checkpoints_ratio' and './DNN training/checkpoints_angle' folders.






