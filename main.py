import torch
import torch.nn as nn
tt_1 = 1
m=torch.jit.load('/media/mxc/zgy/IPIN_2022/GCNv2_SLAM/GCN2/gcn2_640x480.pt')
m.save("/media/mxc/zgy/IPIN_2022/GCNv2_SLAM/GCN2/gcn2_640x480_reload.pt")