#!/usr/bin/env python

'''
A sample script to run classificition using both spatial/temporal nets.
Modify this script as needed.
'''

import numpy as np
import caffe
import math

from VideoSpatialPredictionTest import VideoSpatialPrediction


def softmax(x):
    y = [math.exp(k) for k in x]
    sum_y = math.fsum(y)
    z = [k/sum_y for k in y]

    return z

def main():

    # caffe init
    gpu_id = 0
    caffe.set_device(gpu_id)
    caffe.set_mode_gpu()

    # spatial prediction
    model_def_file = '/home/freedom/Action/caffe-action_recog/models/action_recognition/cuhk_action_spatial_vgg_16_deploy.prototxt'
    model_file = '/home/freedom/Action/caffe-action_recog/cuhk_action_recognition_vgg_16_split1_rgb_iter_10000.caffemodel'
    spatial_net = caffe.Net(model_def_file, model_file, caffe.TEST)



    
    # input video (containing image_*.jpg and flow_*.jpg) and some settings
   
    start_frame = 25
    num_categories = 101
    feature_layer = 'fc8-1'

    num=0
    filename='/home/freedom/Action/caffe-action_recog/examples/action_recognition/dataset_file_examples/val_rgb_new.txt'#label starts from 0
    f=open(filename,'r')
    lines=f.readlines()
    Sum=len(lines)
    for line in lines:
        input_video_dir = line.split()[0]+'/'
        Label=line.split()[2]
    # spatial net prediction
        spatial_mean_file = '/home/freedom/Action/caffe-action_recog/action_matlab/rgb_mean.mat'
        spatial_prediction = VideoSpatialPrediction(
                input_video_dir,
                spatial_mean_file,
                spatial_net,
                num_categories,
                feature_layer,
                start_frame)
        avg_spatial_pred_fc8 = np.mean(spatial_prediction, axis=1)
        avg_spatial_pred = softmax(avg_spatial_pred_fc8)
        if str(avg_spatial_pred.index(max(avg_spatial_pred))) == Label:
            num=num+1
        print num,avg_spatial_pred.index(max(avg_spatial_pred)),Label
    print num,Sum
    accuracy=float(num)/Sum
    print accuracy
        # fused prediction (temporal:spatial = 2:1)


if __name__ == "__main__":
    main()
