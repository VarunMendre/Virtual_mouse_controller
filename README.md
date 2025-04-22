# 🖐️ Gesture-Controlled Virtual Mouse

A Python-based web application that turns your webcam into a **gesture-based virtual mouse controller**! This project leverages **MediaPipe**, **OpenCV**, and **Flask** to recognize hand gestures and map them to system actions like moving the cursor, clicking, scrolling, and controlling volume/brightness.

## 🚀 Features

- 🔁 Control mouse movement using hand gestures  
- 👏 Click, double-click, right-click with specific finger signs  
- 🔊 Adjust system volume and screen brightness using pinch gestures  
- 🌐 Simple web interface to start/stop gesture control (built with Flask + HTML/CSS/JS)

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **Flask**
- **PyAutoGUI**
- **PyCaw** (for volume control)
- **Screen Brightness Control**
- **HTML/CSS/JavaScript** (for UI)

## 💻 How It Works

1. Launches a Flask app with a user-friendly front-end to control the gesture system.
2. When activated, the system captures video from the webcam and uses **MediaPipe** to detect hand landmarks.
3. Hand gestures are analyzed in real time and matched to specific actions like clicks, scrolling, volume/brightness adjustment, and more.
4. The front-end communicates with the backend to toggle the gesture recognition loop on or off.

## ✨ Demo & UI

The interface is clean, minimal, and built with HTML/CSS. It includes:
- Start Gesture Control button
- Stop Gesture Control button
- Status message box

## ⚡ Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Make sure your webcam is accessible and system permissions are granted.

## 📊 Future Improvements
- Add more gestures for additional actions
- Improve detection accuracy in various lighting conditions
- Add multi-hand support for advanced interactions

---

Made with ❤️ using Python & OpenCV

---

Feel free to fork, contribute, or open an issue!

