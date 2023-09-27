from google.colab import drive
drive.mount('/content/drive')

!pip install pyyaml==5.1
!pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
!pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html

import torch
assert torch.__version__.startswith("1.8") 
import torchvision
import cv2
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random
from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

img = cv2.imread("/content/drive/MyDrive/Detectron_Dev/images.jpeg")
# cv2_imshow(img)



"""For Object Detection"""
cfg_object_detection = get_ccfg()
cfg_object_detection.merge_from_file(model_zoo.get_onfig_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml"))
cfg_object_detection.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg_object_detection.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml")

object_detection_predictor = DefaultPredictor(cfg_object_detection)
outputs = object_detection_predictor(img)
# using `Visualizer` to draw the predictions on the image.
v = Visualizer(img[:, :, ::-1], MetadataCatalog.get(cfg_object_detection.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])



"""Instance segmentation"""
cfg_instance_seg = get_cfg()
cfg_instance_seg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg_instance_seg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg_instance_seg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")

instance_segmentation_predictor = DefaultPredictor(cfg_instance_seg)
outputs = instance_segmentation_predictor(img)
# using `Visualizer` to draw the predictions on the image.
v = Visualizer(img[:, :, ::-1], MetadataCatalog.get(cfg_instance_seg.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])


""" Panoptic Segmentation""" 
cfg_panoptic = get_cfg()
cfg_panoptic.merge_from_file(model_zoo.get_config_file("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"))
cfg_panoptic.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml")

panoptic_predictor = DefaultPredictor(cfg_panoptic)
panoptic_seg, segments_info = panoptic_predictor(img)["panoptic_seg"]
# using `Visualizer` to draw the predictions on the image.
v = Visualizer(img[:, :, ::-1], MetadataCatalog.get(cfg_panoptic.DATASETS.TRAIN[0]), scale=1.2)
out = v.draw_panoptic_seg_predictions(panoptic_seg.to("cpu"), segments_info)
cv2_imshow(out.get_image()[:, :, ::-1])
