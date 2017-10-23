# Config file for the Caffe package.
#
# Note:
#   Caffe and this config file depends on opencv,
#   so put `find_package(OpenCV)` before searching Caffe
#   via `find_package(Caffe)`. All other lib/includes
#   dependencies are hard coded in the file
#
# After successful configuration the following variables
# will be defined:
#
#   Caffe_INCLUDE_DIRS - Caffe include directories
#   Caffe_LIBRARIES    - libraries to link against
#   Caffe_DEFINITIONS  - a list of definitions to pass to compiler
#
#   Caffe_HAVE_CUDA    - signals about CUDA support
#   Caffe_HAVE_CUDNN   - signals about cuDNN support


# OpenCV dependency

if(NOT OpenCV_FOUND)
  set(Caffe_OpenCV_CONFIG_PATH "/usr/local/opencv/release")
  if(Caffe_OpenCV_CONFIG_PATH)
    get_filename_component(Caffe_OpenCV_CONFIG_PATH ${Caffe_OpenCV_CONFIG_PATH} ABSOLUTE)

    if(EXISTS ${Caffe_OpenCV_CONFIG_PATH} AND NOT TARGET opencv_core)
      message(STATUS "Caffe: using OpenCV config from ${Caffe_OpenCV_CONFIG_PATH}")
      include(${Caffe_OpenCV_CONFIG_PATH}/OpenCVModules.cmake)
    endif()

  else()
    find_package(OpenCV REQUIRED)
  endif()
  unset(Caffe_OpenCV_CONFIG_PATH)
endif()

# Compute paths
get_filename_component(Caffe_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
set(Caffe_INCLUDE_DIRS "/usr/include;/usr/include/hdf5/serial;/usr/local/cuda/include;/usr/local/include;/usr/local/opencv/release;/usr/local/opencv/include;/usr/local/opencv/include/opencv;/usr/local/opencv/modules/core/include;/usr/local/opencv/modules/flann/include;/usr/local/opencv/modules/imgproc/include;/usr/local/opencv/modules/highgui/include;/usr/local/opencv/modules/features2d/include;/usr/local/opencv/modules/calib3d/include;/usr/local/opencv/modules/ml/include;/usr/local/opencv/modules/video/include;/usr/local/opencv/modules/legacy/include;/usr/local/opencv/modules/objdetect/include;/usr/local/opencv/modules/photo/include;/usr/local/opencv/modules/gpu/include;/usr/local/opencv/modules/ocl/include;/usr/local/opencv/modules/nonfree/include;/usr/local/opencv/modules/contrib/include;/usr/local/opencv/modules/stitching/include;/usr/local/opencv/modules/superres/include;/usr/local/opencv/modules/ts/include;/usr/local/opencv/modules/videostab/include;/opt/intel/mkl/include;/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent;/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent/include;/usr/lib/openmpi/include;/usr/lib/openmpi/include/openmpi")

get_filename_component(__caffe_include "${Caffe_CMAKE_DIR}/../../include" ABSOLUTE)
list(APPEND Caffe_INCLUDE_DIRS ${__caffe_include})
unset(__caffe_include)


# Our library dependencies
if(NOT TARGET caffe AND NOT caffe_BINARY_DIR)
  include("${Caffe_CMAKE_DIR}/CaffeTargets.cmake")
endif()

# List of IMPORTED libs created by CaffeTargets.cmake
set(Caffe_LIBRARIES caffe)

# Definitions
set(Caffe_DEFINITIONS "-DUSE_MKL")

# Cuda support variables
set(Caffe_CPU_ONLY OFF)
set(Caffe_HAVE_CUDA TRUE)
set(Caffe_HAVE_CUDNN TRUE)
