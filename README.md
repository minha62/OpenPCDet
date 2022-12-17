Original Repository: [open-mmlab/OpenPCDet](https://github.com/open-mmlab/OpenPCDet) <br>
pclpy Repository: [davidcaron/pclpy](https://github.com/davidcaron/pclpy)

---

[OpenPCDet Installation](https://velog.io/@bbirong/OpenPCDet-%ED%99%98%EA%B2%BD%EC%84%B8%ED%8C%85)

---

### Change Record

1. Add a file [convert_pcd2bin.py](https://github.com/minha62/OpenPCDet/blob/master/convert_pcd2bin.py) <br>
  📌 need `pclpy`
2. pcdet/datasets/kitti/kitti_dataset.py
3. tools/cfgs/kitti_models/voxel_rcnn_car.yaml
4. tools/cfgs/dataset_configs/kitti_dataset.yaml
5. Add a file [match_label.py](https://github.com/minha62/OpenPCDet/blob/master/match_label.py)
   - label이 없는 calib, image, velodyne 파일 삭제

---

### Commands

- Convert pcd files to bin files
```
$ conda activate pclpy
$ python convert_pcd2bin.py
$ conda deactivate
```

- Generate the data infos <br>
kitti_dataset.yaml에서 DATA_PATH 변경해주기!
```
$ conda activate OpenPCDet
$ cd ~/OpenPCDet
$ python -m pcdet.datasets.kitti.kitti_dataset create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml
```

- Train with a single GPU <br>
voxel_rcnn_car.yaml, pv_rcnn.yaml 사용 <br> 
```
$ cd ~/OpenPCDet/tools
$ python train.py --cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml --batch_size 1 --epochs 10000 
```

- Run the demo with the trained model and custom point cloud data
```
$ cd ~/OpenPCDet/tools
$ python demo.py --cfg_file cfgs/kitti_models/voxel_rcnn_car.yaml \
    --ckpt pv_rcnn_8369.pth \
    --data_path ${POINT_CLOUD_DATA}
```

- Test and evaluate the trained models
   - To test the specific checkpoint, use `--ckpt ${CKPT}`
   - To test all the saved checkpoints, use `--eval_all`
```
$ python test.py --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE} --ckpt ${CKPT}
$ python test.py --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE} --eval_all
```



<주의사항>
> nas에 있는 파일을 불러오는 경우 permission denied 에러 뜰 수 있음. <br>
> 이땐 `conda activate ${환경이름}`후에 python 명령어 쓰지 말고, `sudo ~/anaconda3/envs/${환경이름}/bin/python` 뒤에 명령어 쓰기 <br>
> ex) `python convert_pcd2bin.py` 대신 `sudo ~/anaconda3/envs/pclpy/bin/python convert_pcd2bin.py`

