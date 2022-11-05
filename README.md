Original Repository: [open-mmlab/OpenPCDet](https://github.com/open-mmlab/OpenPCDet) <br>
pclpy Repository: [davidcaron/pclpy](https://github.com/davidcaron/pclpy)

---

[OpenPCDet Installation](https://velog.io/@bbirong/OpenPCDet-%ED%99%98%EA%B2%BD%EC%84%B8%ED%8C%85)

---

### Change Record

1. Add a file [convert_pcd2bin.py](https://github.com/minha62/OpenPCDet/blob/3f85e15a7fd496f2ef6e7696f48eea763521e6ef/convert_pcd2bin.py) <br>
  📌 need `pclpy`
2. pcdet/datasets/kitti/kitti_dataset.py
3. tools/cfgs/kitti_models/voxel_rcnn_car.yaml
4. tools/cfgs/dataset_configs/kitti_dataset.yaml

---

### Commands

- Generate the data infos
```
$ cd ~/OpenPCDet
$ python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml
```

- Train with a single GPU
```
$ cd ~/OpenPCDet/tools
$ python train.py —cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml —batch-size 1 —epochs 10000
```

- Run the demo with the trained model and custom point cloud data
```
$ cd ~/OpenPCDet/demo
$ python demo.py --cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml \
    --ckpt pv_rcnn_8369.pth \
    --data_path ${POINT_CLOUD_DATA}
```
