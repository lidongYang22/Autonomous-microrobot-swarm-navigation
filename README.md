# Autonomous microrobot swarm navigation enabled by DL-based real-time distribution planning
This repository provides information for implementing the deep learning (DL)-based method for real-time microrobot swarm distribution planning and the method for real-time trajectory planning, both applicable for unstructured environments.

[![DOI](https://zenodo.org/badge/427215873.svg)](https://zenodo.org/badge/latestdoi/427215873)

Sample codes includes:
* Training the two DNNs for swarm distribution planning
* Demonstration of the distribution planning in different environments
* Demonstration of the trajectory planning in a channel environment

## Table of contents
1. [Software requirement](##Softwarerequirement)
2. [Dataset](##Dataset)
3. [Sample codes and demonstrations](##Samplecodesanddemonstrations)


## Software requirement

### To run the DNN traning and distribution planning demo programes, the following softwares are needed:
* Python (version 3.6 and above)  
* NumPy
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
1. Download the codes, and the demo program is in the './demo of swarm distribution planning' folder.
2. Run the file './demo of swarm distribution planning/demo.py'.
3. Outputs: the generated planning results will be saved in the './demo of swarm distribution planning/out' folder.

We also provide two additional environments located in the './demo of swarm distribution planning/obstacle environment' folder and the './demo of swarm distribution planning/obstacle and channel environment' folder. To test them, just add the environment files (image and trajecotry) to the './demo of swarm distribution planning' folder, and change the file names in the programe './demo of swarm distribution planning/demo.py' accordingly.

If one want to test their own environments, just create the environment data (image and trajecotry) and use them in the './demo of swarm distribution planning/obstacle environment' folder by following the obove instructions.

### Demo of trajectory planning
Instructions:
1. Download the codes, and the demo program is in './demo of trajectory planning' folder.
2. Run Matlab, and open the file './demo of trajectory planning/example_code_path_planning.m'.
3. Run the file './demo of trajectory planning/example_code_path_planning.m' in Matlab.
4. Outputs: the generated planning results will appear on the screen.

If one want to test the method on different environment morphologies, just add the new environment image to './demo of trajectory planning' folder and change the image name in the program accordingly. In addition, the starting and targeted positions, and tunable parameters should be adjusted, if necessary.
