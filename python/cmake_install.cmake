# Install script for directory: /home/freedom/Action/caffe-action_recog/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python" TYPE FILE FILES
    "/home/freedom/Action/caffe-action_recog/python/convert_to_fully_conv.py"
    "/home/freedom/Action/caffe-action_recog/python/draw_net.py"
    "/home/freedom/Action/caffe-action_recog/python/detect.py"
    "/home/freedom/Action/caffe-action_recog/python/polyak_average.py"
    "/home/freedom/Action/caffe-action_recog/python/classify.py"
    "/home/freedom/Action/caffe-action_recog/python/gen_bn_inference.py"
    "/home/freedom/Action/caffe-action_recog/python/bn_convert_style.py"
    "/home/freedom/Action/caffe-action_recog/python/requirements.txt"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/caffe" TYPE FILE FILES
    "/home/freedom/Action/caffe-action_recog/python/caffe/io.py"
    "/home/freedom/Action/caffe-action_recog/python/caffe/detector.py"
    "/home/freedom/Action/caffe-action_recog/python/caffe/net_spec.py"
    "/home/freedom/Action/caffe-action_recog/python/caffe/__init__.py"
    "/home/freedom/Action/caffe-action_recog/python/caffe/draw.py"
    "/home/freedom/Action/caffe-action_recog/python/caffe/pycaffe.py"
    "/home/freedom/Action/caffe-action_recog/python/caffe/classifier.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/caffe" TYPE SHARED_LIBRARY FILES "/home/freedom/Action/caffe-action_recog/python/CMakeFiles/CMakeRelink.dir/_caffe.so")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/caffe" TYPE DIRECTORY FILES
    "/home/freedom/Action/caffe-action_recog/python/caffe/imagenet"
    "/home/freedom/Action/caffe-action_recog/python/caffe/proto"
    "/home/freedom/Action/caffe-action_recog/python/caffe/test"
    )
endif()

