# ✋ ManoVolume — Gesture-Based Volume Controller

A real-time hand tracking system that lets you control your computer's master volume using simple hand gestures. Built with **OpenCV**, **MediaPipe**, and **pycaw**.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-enabled-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-used-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Features

- 🔍 Detects hand landmarks in real-time using MediaPipe
- 🖐️ Measures distance between fingers to adjust volume
- 🔈 Maps hand distance to system volume via `pycaw`
- ⚡ Displays FPS overlay in the webcam feed

---

## Demo Video
<video controls autoplay muted loop width="600">
  <source src="ManuVolume-Gesture based Volume Changer.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **OpenCV**
- **MediaPipe**
- **pycaw (Windows audio control)**

---

## 🧠 How It Works

1. Detects hand landmarks using MediaPipe.
2. Tracks the distance between thumb and index finger.
3. Normalizes the distance and maps it to system volume range.
4. Sends volume signal using Windows COM interface (`pycaw`).

---

## 📂 Project Structure

```bash
HandTrackingProject/
├── mp_env/                 # Virtual environment (excluded from Git)
├── handTrackingModule.py   # MediaPipe hand tracking wrapper
├── volumeHandControl.py    # Main volume control script
├── .gitignore
├── README.md
└── ManuVolume-Gesture based Volume Changer.mp4
