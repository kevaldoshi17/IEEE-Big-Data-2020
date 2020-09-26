# IEEE-Big-Data-2020
This repository contains source code and trained models for [Road Damage Detection and Classification Challenge](https://rdd2020.sekilab.global/) that was held as one of the 2020 IEEE Big Data Cup.

The best ensemble model achieved mean F1-score of 0.628 (**Ranked 3rd**) on Test 1 dataset and 0.635 (**Ranked 2nd**) on Test 2 dataset of the competition.

- [Quick start](#quick-start)
- [RDCC Dataset Setup](#RDCC-Dataset-Setup)
- [Detection / Submission](#Detection)
- [Training](#Training)

## Quick-start
1. Clone the road-damage-detection repo into $RDD: 

    ```Shell
    git clone https://github.com/kevaldoshi17/IEEE-Big-Data-2020.git
    ```

2. Clone and install the darknet repo as shown here:

    ```Shell
    git clone https://github.com/AlexeyAB/darknet.git
    ```

## RDCC Dataset Setup

1. Register at [RDDC](https://rdd2020.sekilab.global/) website to download competition dataset

2. Augment the dataset using [augment.py](https://github.com/kevaldoshi17/IEEE-Big-Data-2020/blob/master/augment.py)

3. Generate the label files for Darknet using [convert_annotations.py](https://github.com/kevaldoshi17/IEEE-Big-Data-2020/blob/master/convert_annotations.py)

NOTE: It is expected that the Dataset be structured in PASCAL VOC format (images under JPEGImages, XML files under Annotations directory)

## Detection

```Shell
run ./darknet detector train cfg/coco.data cfg/yolov4.cfg /backup/yolov4_1000.weights
```

The ensemble model consists of a base model and 4 semi-base models. 

Base Model: Yolo - Aug - 416x416 it: 14000 test: 416x416

S. Model 1: Yolo - Aug - 416x416 it: [13000-20000] test: 416x416

S. Model 2. Yolo - Aug - 608x608 it: [14000-20000] test: 608x608

S. Model 3. Yolo - Aug - 608x608 it: [15000-20000] test: 416x416

S. Model 4. Yolo - No Aug - 416x416 it: [15000-18000] test: 416x416

Save each S. Model at intervals of 1000 between the limits shown above. Save all of the models in the folder [model](https://github.com/kevaldoshi17/IEEE-Big-Data-2020/tree/master/models).


The models can be downloaded from here:https://drive.google.com/file/d/13wgjGXkYm_55ixO_cH7fbOrBjJZ1X8-O/view?usp=sharing
