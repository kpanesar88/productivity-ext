"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

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

try:
    while True:
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

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (blue, green, red), 2)

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

        cv2.putText(frame, f"Total Time:  {int(total_hour):01d}:{int(total_minutes):02d}:{int(total_seconds):02d}" , (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 1)
        cv2.putText(frame, f"Time Focused:  {int(focus_hour):01d}:{int(focus_minutes):02d}:{int(focus_seconds):02d}" , (90, 170), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 1)

        cv2.imshow("GazeTracker", frame)

        if cv2.waitKey(1) == 27:
            break

except KeyboardInterrupt:
    totalSW.stop()
    totalTime = totalSW.duration
    print("Total Time: " + str(totalTime))
    
    percentage = (focus_seconds / totalTime ) * 100
    print("Percentage Focused: " + str(int(percentage)) + "%")


    webcam.release()
    cv2.destroyAllWindows()
