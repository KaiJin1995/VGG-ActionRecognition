#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:43:33 2017

@author: freedom
"""


import numpy as np
import caffe
import math


from VideoSpatialPredictionTest import VideoSpatialPrediction
from VideoTemporalPredictionTest import VideoTemporalPrediction


def softmax(x):
    y = [math.exp(k) for k in x]
    sum_y = math.fsum(y)
    z = [k/sum_y for k in y]

    return z
def main():

    # caffe init
    gpu_id = 3
    caffe.set_device(gpu_id)
    caffe.set_mode_gpu()

    # spatial prediction
    model_def_file = '/home/freedom/Action/caffe-action_recog/models/action_recognition/cuhk_action_spatial_vgg_16_deploy.prototxt'
    model_file = '/home/freedom/Action/caffe-action_recog/cuhk_action_recognition_vgg_16_split1_rgb_iter_10000.caffemodel'
    spatial_net = caffe.Net(model_def_file, model_file, caffe.TEST)
    # temporal prediction
    model_def_file = '/home/freedom/Action/caffe-action_recog/models/action_recognition/cuhk_action_temporal_vgg_16_flow_deploy.prototxt'
    model_file = '/home/freedom/Action/caffe-action_recog/CaffeModelTemporalNew/split1_flow_nochange_iter_30000.caffemodel'
    temporal_net = caffe.Net(model_def_file, model_file, caffe.TEST)

    # input video (containing image_*.jpg and flow_*.jpg) and some settings
    start_frame = 0
    num_categories = 101
    
    feature_layer_spatial = 'fc8-1'
    feature_layer_temporal = 'fc8-2'
    
    num=0
    filename_temporal='/home/freedom/Action/caffe-action_recog/examples/action_recognition/dataset_file_examples/val_flow_new.txt'#label starts from 0
    f_t=open(filename_temporal,'r')
    lines_t=f_t.readlines()
    
    filename_spatial='/home/freedom/Action/caffe-action_recog/examples/action_recognition/dataset_file_examples/val_rgb_new.txt'#label starts from 0
    f_s=open(filename_spatial,'r')
    lines_s=f_s.readlines()
    
    Sum=len(lines_t)
    spatial_mean_file = '/home/freedom/Action/caffe-action_recog/action_matlab/rgb_mean.mat'
    temporal_mean_file = '/home/freedom/Action/caffe-action_recog/action_matlab/flow_mean.mat'
    for i in range(Sum):
        input_svideo_dir = lines_s[i].split()[0]+'/'
        input_tvideo_dir = lines_t[i].split()[0]+'/'
        Label=lines_s[i].split()[2]
        temporal_prediction = VideoTemporalPrediction(
            input_tvideo_dir,
            temporal_mean_file,
            temporal_net,
            num_categories,
            feature_layer_temporal,
            start_frame)
        
        spatial_prediction = VideoSpatialPrediction(
                input_svideo_dir,
                spatial_mean_file,
                spatial_net,
                num_categories,
                feature_layer_spatial,
                start_frame)
        
        
        avg_temporal_pred_fc8 = np.mean(temporal_prediction, axis=1)
        avg_temporal_pred = softmax(avg_temporal_pred_fc8)
        
        
        avg_spatial_pred_fc8 = np.mean(spatial_prediction, axis=1)
        avg_spatial_pred = softmax(avg_spatial_pred_fc8)
        
        
        fused_pred = np.array(avg_temporal_pred) * 2./3 + \
                     np.array(avg_spatial_pred) * 1./3
        #if str(fused_pred.index(max(fused_pred))) == Label:
        #    num=num+1
        if str(np.where(fused_pred==fused_pred.max())[0][0])==Label:
            num=num+1
        
        print num,np.where(fused_pred==fused_pred.max())[0][0],Label
    print num,Sum
    accuracy=float(num)/Sum
    print accuracy
    
    
    
if __name__ == "__main__":
    main()
    
    
    