from flask import Flask, render_template, request, jsonify
import threading
import cv2
from Gesture_Controller import GestureController  # Import your GestureController class

app = Flask(__name__)

# Global variable for gesture controller
gc_instance = None
gesture_thread = None

def start_gesture_controller():
    global gc_instance
    gc_instance = GestureController()
    gc_instance.start()

# @app.route('/')
# def index():
#     return render_template('index.html')  # Create an index.html for UI

@app.route('/')
def index():
    return render_template('index.html')  # Flask automatically looks in the templates folder


@app.route('/start', methods=['POST'])
def start_gesture():
    global gesture_thread
    if gesture_thread is None or not gesture_thread.is_alive():
        gesture_thread = threading.Thread(target=start_gesture_controller)
        gesture_thread.start()
        return jsonify({'status': 'Gesture control started'})
    return jsonify({'status': 'Already running'})

@app.route('/stop', methods=['POST'])
def stop_gesture():
    global gc_instance
    if gc_instance:
        gc_instance.gc_mode = 0  # Set to 0 to stop loop
        gc_instance.cap.release()  # Release camera
        cv2.destroyAllWindows()  # Close OpenCV windows
        gc_instance = None  # Reset instance
        return jsonify({'status': 'Gesture control stopped'})
    return jsonify({'status': 'No active gesture controller'})

if __name__ == '__main__':
    app.run(debug=True)
