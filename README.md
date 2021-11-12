# Autonomous microrobot swarm navigation enabled by DL-based real-time distribution planning
This repository provides information for implementing the DL-based method for real-time microrobot swarm distribution planning and the method for real-time trajectory planning, both applicable for unstructured environments.

## Table of contents
1. [Software requirement](#Softwarerequirement)
2. [Datasets](#Datasets)
3. [Experiments](#Experiments)
4. [Citation](#citation)


# Software requirement

# Reference
Kai Fukami (UCLA), Romit Maulik (ANL), Nesar Ramachandra (ANL), Koji Fukagata (Keio), and Kunihiko Taira (UCLA), "Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning," Nature Machine Intelligence, accepted, preprint: [arXiv:2101.00554](https://arxiv.org/abs/2101.00554), 2021

# Information
Author: [Kai Fukami](https://scholar.google.co.jp/citations?user=ipJb8qcAAAAJ&hl=en) (UCLA)

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
