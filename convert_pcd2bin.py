import pclpy
import pclpy.pcl as pcl
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

    pcd = pcdreader.read(input_path, pc)
    points = pc.xyz

    p = from_xyz_to_xyzi(points)
    return np.array(list(p), dtype = np.float32)

def save_bin_from_pc(points, bin_path):
    points.tofile(bin_path)


#file_list = glob.glob(f'/home/smha/vs-nas/OpenPCDet/data/kitti1101/training/pcd/*.pcd', recursive=True)
file_list = os.listdir('home/smha/vs-nas/OpenPCDet/data/kitti1101/training/pcd/*.pcd')

for file_path in file_list:
    points = load_pc_from_pcd(file_path)

    split_list = file_path.split("/")
    bin_path = split_list[0]+"/"+split_list[1]+"/"+split_list[2]+"/"+split_list[3]+"/"+split_list[4]+"/"+"new_data"+"/"+"kitti_1103"+"/"+"bin"+"/"

    if not os.path.exists(bin_path):
        os.makedirs(bin_path)

    bin_name = split_list[8].replace('.pcd', '.bin')
    save_bin_from_pc(points, bin_path + bin_name)
