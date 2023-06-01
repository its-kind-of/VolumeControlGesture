# Hand Gesture Volume Control

This is a Python script that uses hand gesture recognition to control the system volume. It utilizes the OpenCV, Mediapipe, and pycaw libraries to detect hand landmarks, calculate the distance between two specific landmarks, and adjust the system volume accordingly.

## Requirements

- Python 3.6+
- OpenCV
- Mediapipe
- pycaw
- comtypes

You can install the required libraries using pip:
```
pip install opencv-python mediapipe pycaw comtypes
```

## Usage

1. Connect a webcam to your computer.
2. Run the `hand_gesture_volume_control.py` script.
3. The script will open a window showing the webcam feed.
4. Hold your hand up in front of the camera with your palm facing towards the camera.
5. Adjust the distance between your thumb and index finger to control the volume.
   - Move your thumb and index finger closer together to decrease the volume.
   - Move your thumb and index finger farther apart to increase the volume.
   - The volume level will be displayed on the screen.
   - A green circle will appear when the distance is small, indicating a low volume.
   - A red circle will appear when the distance is large, indicating a high volume.

## Customization

- You can adjust the camera width and height by modifying the `wCam` and `hCam` variables in the script.
- The hand gesture detection parameters can be tweaked by modifying the values in the `HandTrackingModule.py` file.
- Feel free to customize the UI and add additional functionality based on your requirements.
