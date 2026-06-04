# finger-counter-cv
# Finger Counter CV

A real-time finger counting system using Python, OpenCV and MediaPipe.
Detects and tracks both hands simultaneously, counts fingers independently
for each hand, and recognizes hand gestures.

## Features
- Multi-hand detection (up to 2 hands)
- Left & right hand recognition
- Per-hand finger count displayed live
- Gesture recognition (Fist, Peace, Thumbs Up, Pointing, Rock On...)

## Requirements
Install dependencies with:
pip install opencv-python mediapipe

## How to Run
python AdvancedFingerCounter.py

## Project Structure
- `AdvancedFingerCounter.py` — main script
- `HandTrackingModule.py` — reusable hand tracking module

## Built With
- Python
- OpenCV
- MediaPipe
