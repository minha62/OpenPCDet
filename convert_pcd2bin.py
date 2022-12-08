# command: $ sudo ~/anaconda3/envs/pclpy/bin/python convert_pcd2bin.py --path '${parent folder path of pcd folder}'

import pclpy
import pclpy.pcl as pcl
import numpy as np
import os
import glob
import shutil
from absl import app, flags
from absl.flags import FLAGS


flags.DEFINE_string('path', '/home/smha/ts_backup2_249/OpenPCDet/gumsu_ori_data/kitti/training/20221020/', 'parent folder path of pcd folder')


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


def main(argv):
    pcd_path = os.path.join(FLAGS.path, 'pcd/*.pcd')

    # list of pcd files' path
    pcd_list = glob.glob(pcd_path, recursive=True)

    i = 1 # for checking the progress of conversion

    for pcd in pcd_list:
        # load xyzi points from pcd
        points = load_pc_from_pcd(pcd)

        bin_path = os.path.join(FLAGS.path, 'velodyne/')

        if not os.path.exists(bin_path):
            os.makedirs(bin_path)

        
        splited_pcd_path = pcd.split("/")

        # convert the file extension (PCD -> BIN)
        bin_name = splited_pcd_path[-1].replace('.pcd', '.bin')
        
        save_bin_from_pc(points, bin_path + bin_name)

        # print progress
        print(f'{i} / {len(file_list)}')
        i += 1

app.run(main)
