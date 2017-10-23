#!/usr/bin/env python

'''
A sample script to run classificition using both spatial/temporal nets.
Modify this script as needed.
'''

import numpy as np
import caffe
import math

from VideoTemporalPredictionTest import VideoTemporalPrediction

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


    # temporal prediction
    model_def_file = '/home/freedom/Action/caffe-action_recog/models/action_recognition/cuhk_action_temporal_vgg_16_flow_deploy.prototxt'
    model_file = '/home/freedom/Action/caffe-action_recog/CaffeModelTemporalNew/split1_flow_nochange_iter_30000.caffemodel'
    temporal_net = caffe.Net(model_def_file, model_file, caffe.TEST)

    # input video (containing image_*.jpg and flow_*.jpg) and some settings
    start_frame = 0
    num_categories = 101
    feature_layer = 'fc8-2'
    
    
    
    
    num=0
    filename='/home/freedom/Action/caffe-action_recog/examples/action_recognition/dataset_file_examples/val_flow_new.txt'#label starts from 0
    f=open(filename,'r')
    lines=f.readlines()
    Sum=len(lines)
    for line in lines:
        input_video_dir = line.split()[0]+'/'
        Label=line.split()[2]
    # spatial net prediction

    # temporal net prediction
        temporal_mean_file = '/home/freedom/Action/caffe-action_recog/action_matlab/flow_mean.mat'
        temporal_prediction = VideoTemporalPrediction(
            input_video_dir,
            temporal_mean_file,
            temporal_net,
            num_categories,
            feature_layer,
            start_frame)
        avg_temporal_pred_fc8 = np.mean(temporal_prediction, axis=1)
        avg_temporal_pred = softmax(avg_temporal_pred_fc8)
        if str(avg_temporal_pred.index(max(avg_temporal_pred))) == Label:
            num=num+1
        print num,avg_temporal_pred.index(max(avg_temporal_pred)),Label
    print num,Sum
    accuracy=float(num)/Sum
    print accuracy


if __name__ == "__main__":
    main()
