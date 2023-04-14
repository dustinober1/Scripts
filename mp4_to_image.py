import cv2

# Open the mp4 file
vidcap = cv2.VideoCapture('F224.mp4')

# Set the frame rate of the video
fps = vidcap.get(cv2.CAP_PROP_FPS)

# Set the interval time (in seconds) between each frame to capture
interval = 0.5

# Set the initial time to capture the first frame
time_to_capture = 0

while True:
    # Set the frame number to capture based on the time to capture
    frame_number = int(round(time_to_capture * fps))

    # Set the video to the frame number to capture
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Capture the frame
    success, image = vidcap.read()

    # If a frame was successfully captured, save it as an image
    if success:
        cv2.imwrite("F2206_" + str(frame_number) + ".jpg", image)

    # Increase the time to capture by the interval time
    time_to_capture += interval

    # If the next frame to capture is beyond the end of the video, break the loop
    if frame_number >= vidcap.get(cv2.CAP_PROP_FRAME_COUNT):
        break
