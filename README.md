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
1. Voronoi-CNN-cy.py (Example 1)
2. Voronoi-CNN-NOAA.py (Example 2)
3. Voronoi-CNN-ch2Dxysec.py (Example 3)

Authors provide no guarantees for this code. Use as-is and for academic research use only; no commercial use allowed without permission. The code is written for educational clarity and not for speed.
Training data for each example can be downloaded from Google Drive. Links of GD are provided in each sample code. 



