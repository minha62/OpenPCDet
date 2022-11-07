import pclpy
from pclpy import pcl
import numpy as np
import os
import glob
import shutil

def from_xyz_to_xyzi(points):
    row, column = points.shape
    intensity = np.zeros((row, 1), dtype = np.float32)
    points = np.concatenate((points, intensity), axis = 1)
    return points

def load_pc_from_pcd(input_path):
    pcdreader = pcl.io.PCDReader()
    pc = pcl.PointCloud.PointXYZ()

    pcdreader.read(input_path, pc)
    points = pc.xyz

    p = from_xyz_to_xyzi(points)
    return np.array(list(p), dtype = np.float32)

def save_bin_from_pc(points, bin_path):
    points.tofile(bin_path)


#file_list = glob.glob(f'/home/smha/vs-nas/OpenPCDet/data/kitti1101/training/pcd/*.pcd', recursive=True)
# file_path = '/home/smha/vs-nas/OpenPCDet/data/kitti1101/training/pcd/'
file_path = '/home/smha/vs-nas/OpenPCDet/sunset_cloudy_normal_20220803_094139_santafe/pcd/'
file_list = os.listdir(file_path)
file_num = len(file_list)
i = 1

for file in file_list:
    print(f"{i} / {file_num}")
    i += 1
    points = load_pc_from_pcd(file_path + file)
    # print('file_path',file_path)

    split_list = file_path.split("/")
    # bin_path = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+"new_data"+"/"+"kitti_1103"+"/"+"bin"+"/"
    bin_path = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+"new_data"+"/"+"kitti_1107"+"/"+split_list[5]+"/"+"bin"+"/"
    if not os.path.exists(bin_path):
        os.makedirs(bin_path)

    bin_name = file.replace('.pcd', '.bin')
    save_bin_from_pc(points, bin_path + bin_name)
