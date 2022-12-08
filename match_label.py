# commands: sudo ~/anaconda3/envs/OpenPCDet/bin/python rmimg.py --path '~/ts_backup2_249/1205OpenPCDet/sm_data/training2' --data 'calib'

import glob
import shutil
import os
from absl import app, flags
from absl.flags import FLAGS


flags.DEFINE_string('path', '/home/smha/ts_backup2_249/1205OpenPCDet/gumsu_ori_data/kitti/training/day_sunny_normal_20220901/', '')
flags.DEFINE_string('data', 'calib', 'calib or image or velodyne')
 
data = {'calib':'.txt', 'image_2':'.jpg', 'velodyne':'.bin', 'label_2':'.txt'}

def main(argv):
    files = glob.glob(os.path.join(FLAGS.path, FLAGS.data, '*' + data[FLAGS.data]))

    for file in files:
        tmp = file.replace(FLAGS.data, 'label_2')

        if FLAGS.data != 'calib':
            tmp = tmp.replace(data[FLAGS.data], data['label_2'])
        
        if not os.path.exists(tmp):
            os.remove(file)
    
app.run(main)
