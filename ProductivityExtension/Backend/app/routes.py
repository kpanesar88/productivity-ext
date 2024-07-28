from flask import Flask, render_template, jsonify, Blueprint, Response

import cv2
from gaze_tracking import GazeTracking
from stopwatch import Stopwatch

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

focusSW = Stopwatch(3)
focusSW.stop()
focusSW.reset()

totalSW = Stopwatch(3)
totalSW.stop()
totalSW.reset()
totalSW.start()

main_bp = Blueprint('main', __name__)

# def generate_frames():
#     camera = cv2.VideoCapture(0)
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main_bp.route("/", methods=['GET', 'POST'])
def index():
  return render_template("home.html")

# @main_bp.route('/video_feed')
# def video_feed():
#   return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@main_bp.route("/track", methods=['GET'])
def track():
  # We get a new frame from the webcam
  _, frame = webcam.read()

  # We send this frame to GazeTracking to analyze it
  gaze.refresh(frame)

  frame = gaze.annotated_frame()
  text = ""
  red = 0
  blue = 0
  green = 0

  if gaze.is_center():
      focusSW.start()
      text = "Focused"
      green = 255
  else:
      focusSW.stop()
      text = "Distracted"
      red = 255
  focus_seconds = focusSW.duration
  focus_seconds = focus_seconds % (24 * 3600)
  focus_hour = focus_seconds // 3600
  focus_seconds %= 3600
  focus_minutes = focus_seconds // 60
  focus_seconds %= 60

  total_seconds = totalSW.duration
  total_seconds = total_seconds % (24 * 3600)
  total_hour = total_seconds // 3600
  total_seconds %= 3600
  total_minutes = total_seconds // 60
  total_seconds %= 60
  
  
  return jsonify(time_elapsed=total_seconds, time_focused=focus_seconds)


# if __name__ == '__main__':
#     app.run(debug=True)