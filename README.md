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
