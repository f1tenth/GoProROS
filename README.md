# GoProROS
A simple ROS wrapper for publishing images from a GoPRO.
To start off, you will need to install the gopro webcam cli to trigger the GoPro into webcam mode:


#### GoPro Webcam cli tool
```bash
sudo apt-get install v4l-utils
sudo apt install ffmpeg v4l2loopback-dkms curl vlc
git submodule update --init --recursive
cd src/gopro_as_webcam_on_linux
sudo ./install.sh
sudo gopro webcam
```

To run the GoPro as a standard webcam (i.e with zoom/opencv) you can run `ffmpeg -nostdin -threads 1 -i 'udp://@0.0.0.0:8554?overrun_nonfatal=1&fifo_size=50000000' -f:v mpegts -fflags nobuffer -vf format=yuv420p -f v4l2 /dev/video42`
With this in place, we can proceed to running the ROS node for publishing the images from the GoPro. Be sure to not be using the GoPro in any other software (zoom/opencv/meets/etc...). 

#### ROS GoPro Package 
#### Adding the Package to Your Workspace and Building It

First, add the GoProROS package to your workspace:

```bash
cd ~/your_workspace/src
git clone https://github.com/your_username/GoProROS.git
```

Then, build the package using colcon:

```bash
cd ~/your_workspace
colcon build --packages-select GoProROS
```

#### Running the GoPro Node
Source your workspace and run the GoPro node:

```bash
source ~/your_workspace/install/setup.bash
ros2 run gopro_ros gopro_ros
```

Make sure you have the GoPro running in webcam mode before running the node. The node will publish the images from the GoPro to the `/gopro/image_raw` topic. You can view the images using the `rqt_image_view` tool:

```bash
ros2 run rqt_image_view rqt_image_view
```

Alternatively, you can visualize this topic in rviz2.
