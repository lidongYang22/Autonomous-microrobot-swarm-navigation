# Autonomous microrobot swarm navigation enabled by DL-based real-time distribution planning
This repository provides information for implementing the deep learning (DL)-based method for real-time microrobot swarm distribution planning and the method for real-time trajectory planning, both applicable for unstructured environments.

Sample codes includes:
* Training the two DNNs for swarm distribution planning
* Demonstration of the distribution planning in a channel environment
* Demonstration of the trajectory planning

## Table of contents
1. [Software requirement](##Softwarerequirement)
2. [Dataset](#Dataset)
3. [Sample codes and demonstrations](#Samplecodesanddemonstrations)
4. [Citation](#citation)


## Software requirement

### To run the DNN traning and distribution planning demo programes, the following softwares are needed:
* Python (version 3.6 and above)  
* numpy
* Pytorch

### To run the trajectory planning demo program, the following softwares are needed:
* Matlab (version 2016 and above)  

# Dataset

# Sample codes and demonstrations

This repository contains

1. Voronoi-CNN-cy.py (Example 1)
2. Voronoi-CNN-NOAA.py (Example 2)
3. Voronoi-CNN-ch2Dxysec.py (Example 3)

Authors provide no guarantees for this code. Use as-is and for academic research use only; no commercial use allowed without permission. The code is written for educational clarity and not for speed.
Training data for each example can be downloaded from Google Drive. Links of GD are provided in each sample code. 

# Data sets
Sample training data sets used in the present study are available as follows:

[Example 1 (two-dimensional cylinder wake):](https://drive.google.com/drive/folders/1K7upSyHAIVtsyNAqe6P8TY1nS5WpxJ2c?usp=sharing),
[Example 2 (NOAA sea surface temperature):](https://drive.google.com/drive/folders/1pVW4epkeHkT2WHZB7Dym5IURcfOP4cXu?usp=sharing),
[Example 3 (turbulent channel flow):](https://drive.google.com/drive/folders/1xIY_jIu-hNcRY-TTf4oYX1Xg4_fx8ZvD?usp=sharing)).


# Requirements
* Python 3.x  
* keras  
* tensorflow
* sklearn
* numpy
* pandas
