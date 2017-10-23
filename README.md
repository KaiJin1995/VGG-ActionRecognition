###**致谢：该代码是对yjxiong代码的改进，弥补了里面的些许错误，非常感谢yjxiong的开源精神**

###**前言**：

该代码是在caffe框架运行，是yjxiong的https://github.com/yjxiong/caffe 的一些改进，caffe是用的他的修改版，即里面包含了openmpi多线程，具体使用方法参考上面的网址。
由于他的caffe里面东西较多，在亲自移植代码后，发现有许多小错误，对其进行了修改。
该代码在移植的过程中，使用了4块GTX1080Ti的显卡。

###**使用**：

大部分跟yjxiong所言一致，只是有部分地方进行了修正。

- models/action_recognition文件夹下有多个prototxt文件，其中flow.solver文件有两个，New版本是我修改后的版本，是与论文一致的版本。不带New的版本是原版的solver文件。区别在于是否将图片resize成340*256和scale_ratios是否含有0.66。原版将其省略，而我将其加上。虽然准确率并没有太大的变化。因此，**使用带New的**.
 
- action_python/下有许多测试文件，测试temporal net使用**demoTemporal.py**，测试spatial net使用**demoSpatial.py**。测试temporal+spatial使用**demoTemporalSpatial.py**。文件全部调用的是VideoSpatialPredictionTest.py 和VideoTemporalPredictionTest.py 。原版的有一些错误，因此改成使用后缀有Test的。

- examples/action_recognition/dataset_file_examples/ 下的txt文件修改。因为用之前我的github中的denseflow提取出的rgb图和optical flow 图的个数与txt中的个数不能对应。对原版的txt文件中视频提取图片的帧数进行了修改。否则，若提取的图片小于txt文件中的视频帧数，网络输入图片的时候，将会出现找不到某些图片的报错。**因此，使用后缀带new的。**

上面三个是本系统的关键，另外还对caffe的源码进行了修改，这跟https://github.com/yjxiong/caffe 所说的修改是一致的。


最终可以根据本代码直接进行，进行训练的时候，在caffe根目录下，输入mpirun -np 4 ./install/bin/caffe train --solver=<Your Solver File>  -weights=< Pretrained caffemodel>即可运行。
(当然，要提取安装openmpi)。

具体的准确率情况参考csdn博客:http://blog.csdn.net/small_ARM/article/details/78283205


###**Citation** 

You are encouraged to also cite one of the following papers if you find this repo helpful



> @article{MultiGPUCaffe2015,
  author    = {Limin Wang and
               Yuanjun Xiong and
               Zhe Wang and
               Yu Qiao},
  title     = {Towards Good Practices for Very Deep Two-Stream ConvNets},
  journal   = {CoRR},
  volume    = {abs/1507.02159},
  year      = {2015},
  url       = {http://arxiv.org/abs/1507.02159},
}







Following is the original README of Caffe.

###**Caffe**


Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by the Berkeley Vision and Learning Center (BVLC) and community contributors.

Check out the project site for all the details like

    DIY Deep Learning for Vision with Caffe
    Tutorial Documentation
    BVLC reference models and the community model zoo
    Installation instructions

and step-by-step examples.

Join the chat at https://gitter.im/BVLC/caffe

Please join the caffe-users group or gitter chat to ask questions and talk about methods and models. Framework development discussions and thorough bug reports are collected on Issues.

Happy brewing!
###**License and Citation**

Caffe is released under the BSD 2-Clause license. The BVLC reference models are released for unrestricted use.

Please cite Caffe in your publications if it helps your research:

> @article{jia2014caffe,
  Author = {Jia, Yangqing and Shelhamer, Evan and Donahue, Jeff and Karayev, Sergey and Long, Jonathan and Girshick, Ross and Guadarrama, Sergio and Darrell, Trevor},
  Journal = {arXiv preprint arXiv:1408.5093},
  Title = {Caffe: Convolutional Architecture for Fast Feature Embedding},
  Year = {2014}
}
