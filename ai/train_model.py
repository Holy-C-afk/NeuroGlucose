import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

def train_model():
    # Load the dataset (replace 'data.csv' with your actual dataset file or database query)
    data = pd.read_csv('data.csv')  # Ensure this file exists in your project directory
    print("Dataset loaded successfully.")

    # Define features (X) and target (y)
    X = data[['feature1', 'feature2', 'feature3']]  # Replace with actual feature column names
    y = data['glucose_level']  # Replace with the actual target column name

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Data split into training and testing sets.")

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model training completed.")

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error on test data: {mse}")

    # Save the trained model to a file
    joblib.dump(model, 'trained_model.pkl')
    print("Trained model saved as 'trained_model.pkl'.")

if __name__ == "__main__":
    train_model()