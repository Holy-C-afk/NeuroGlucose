import cv2
import numpy as np

def preprocess_frame(frame):
    """
    Preprocess a video frame for eye movement analysis.
    This function converts the frame to grayscale and applies Gaussian blur.
    """
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    return blurred_frame

def detect_pupil_dilation(frame):
    """
    Detect pupil dilation from a video frame.
    This is a placeholder function that uses simple thresholding to detect the pupil.
    """
    processed_frame = preprocess_frame(frame)
    _, thresholded = cv2.threshold(processed_frame, 50, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        return radius  # Return the radius of the detected pupil
    return 0

def extract_eye_movement_features(video_path):
    """
    Extract eye movement features from a video file.
    This function processes each frame of the video and calculates features like pupil dilation.
    """
    cap = cv2.VideoCapture(video_path)
    features = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        pupil_dilation = detect_pupil_dilation(frame)
        features.append(pupil_dilation)

    cap.release()
    return features

if __name__ == "__main__":
    # Example usage
    video_path = "example_video.mp4"  # Replace with the path to your video file
    features = extract_eye_movement_features(video_path)
    print("Extracted features:", features)