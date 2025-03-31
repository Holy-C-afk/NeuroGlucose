import numpy as np
from sklearn.externals import joblib
from .eye_analysis import extract_eye_movement_features

def predict_glucose_variation(video_path):
    """
    Predict blood sugar variation using features extracted from eye movement video.
    """
    # Step 1: Extract features from the video
    features = extract_eye_movement_features(video_path)
    print("Extracted features:", features)

    # Step 2: Load the trained model
    model = joblib.load('trained_model.pkl')  # Ensure this file exists in your project directory
    print("Trained model loaded successfully.")

    # Step 3: Prepare features for prediction
    # Convert the features into a format suitable for the model (e.g., mean, std, etc.)
    feature_array = np.array(features).reshape(1, -1)  # Example: reshape for a single prediction

    # Step 4: Make a prediction
    glucose_variation = model.predict(feature_array)
    print("Predicted glucose variation:", glucose_variation)

    return glucose_variation

if __name__ == "__main__":
    # Example usage
    video_path = "example_video.mp4"  # Replace with the path to your video file
    prediction = predict_glucose_variation(video_path)
    print("Blood sugar variation prediction:", prediction)