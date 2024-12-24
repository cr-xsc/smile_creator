# smile_creator

## Demo
![smile_creator](https://github.com/user-attachments/assets/fe0fca9a-33d3-499c-8b9e-09b607ac0d71)

[youtube](https://www.youtube.com/watch?v=7SpeD7yOXh8)


## table of contents
- [Operation overview](https://github.com/cr-xsc/smile_creator/blob/main/README.md#operation-overview)
- [Prerequisites](https://github.com/cr-xsc/smile_creator/blob/main/README.md#prerequisites)
- [Installation](https://github.com/cr-xsc/smile_creator/blob/main/README.md#installation)
- [Usage](https://github.com/cr-xsc/smile_creator/blob/main/README.md#usage)


## Operation overview
The eye_mosaic project detects the front face of a person from the image of a USB webcam or CSI camera connected to Jetson nano,Mosaic the eyes or the entire face in real time.
Multiple faces can be detected at the same time, and the coarseness of the mosaic can be changed as an option. 


## Prerequisites

- NVIDIA Jetson Nano Developer Kit
- USB Web Camera or Raspberry Pi Camera V2
- NVIDIA JetPack 4.6.1 or later

## Installation
Install this application.
   ```
   $ git clone https://github.com/CosmorootMcs/smile_creator
   ```
Install the dependent modules.
   ```
   $ pip3 install -r requirements.txt
   ```

## Usage

Find the camera number and make a note of it.
   ```
   $ ls -la /dev/video*
   ```
Navigate to the downloaded folder.
   ```
   $ cd smile_creator
   ```
Run the program with the following command. 
Use the camera number you noted down. To end the program, press Q.

   ```
   $ python3 smile_creator.py [--camera CAMERA_NUM]
                              [--csi]
                              [--smile]
                              [-h] 
                         
     optional arguments:
       -c CAMERA_NUM, --camera CAMERA_NUM
                          camera number
       --csi              use CSI camera
       -s, --smile        Smile detection
       -h, --help         show this help message and exit
   ```

When you execute the command, the camera will output video and if a face is captured on camera, 
it will detect whether or not the person is smiling.

![398385607-0e53c046-e2a7-47f8-9328-ee58f4d02827](https://github.com/user-attachments/assets/1e8b42a4-6437-4cd4-abf6-f4f3394b7554)

#### Option
Display the help screen
   ```
   -h, --help
   ```

Add this option if you use a CSI camera
   ```
   --csi
   ```

Smile Detection
   ```
   -s, --smile
   ```
#### Command example
csi camera
   ```
   $ python3 eye_mosaic.py --csi -s
   ```
