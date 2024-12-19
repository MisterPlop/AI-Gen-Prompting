## Prompt : 
# Create an API, using FLASK to predict avocado prices.
# Use the exported regression model 'avocado_pipeline.pkl' with pickle
# Dynamically handle one-hot encoded categorical features to ensure flexible predictions.
# Import the pipeline using pickle
# Preprocess input data matching the original model's training
# Dynamically generate one-hot encoded columns for 'type' and 'region'.
# Create a robust prediction endpoint that handles various input scenarios
# Model Context:
# - Predicts average avocado prices using multiple features
# - Target variable: AveragePrice
# - Features include: 
#     * Numerical: Quality1, Quality2, Quality3, Small Bags, Large Bags, XLarge Bags, year
#     * Categorical: type, region
# API Specifications:
# - Endpoint: localhost/avocado/predict
# - Method: POST
# - Input: JSON body with required features
# - Output: Predicted average price as a float, 2 decimals
# - Error handling for missing or incorrect features

# Additional Handling:
# - Dynamically create full feature matrix including all one-hot encoded columns
# - Convert prediction to standard Python float for JSON serialization
# - Provide informative error messages

# Validation Steps:
# - Check for missing required features
# - Automatically generate one-hot encoded columns based on input
# - Ensure preprocessing matches original model training

# Recommended Imports:
# - flask
# - pickle
# - pandas
# - numpy
# - sklearn metrics

# Comments Required:
# - Feature list
# - Endpoint usage instructions
# - Error handling explanation

from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pickle

app = Flask(__name__)

# Load the saved pipeline
try:
    with open('avocado_price_predictor.pkl', 'rb') as file:
        pipeline = pickle.load(file)
except FileNotFoundError:
    raise FileNotFoundError("Model file 'avocado_price_predictor.pkl' not found. Ensure the model file is in the correct location.")

# Define the expected features
NUMERIC_FEATURES = [
    'Quality1', 'Quality2', 'Quality3',
    'Small Bags', 'Large Bags', 'XLarge Bags',
    'year'
]

CATEGORICAL_FEATURES = ['type', 'region']

def validate_input(data):
    """
    Validate that all required features are present in the input data.
    Returns: tuple (is_valid, error_message)
    """
    missing_features = []
    
    # Check numeric features
    for feature in NUMERIC_FEATURES:
        if feature not in data:
            missing_features.append(feature)
            
    # Check categorical features
    for feature in CATEGORICAL_FEATURES:
        if feature not in data:
            missing_features.append(feature)
    
    if missing_features:
        return False, f"Missing required features: {', '.join(missing_features)}"
    
    return True, None

def preprocess_input(data):
    """
    Preprocess the input data to match the format expected by the model.
    Handles both numeric and categorical features.
    """
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([data])
        
        # Ensure all numeric features are float
        for feature in NUMERIC_FEATURES:
            input_df[feature] = input_df[feature].astype(float)
            
        return input_df
        
    except ValueError as e:
        raise ValueError(f"Error preprocessing input data: {str(e)}")

@app.route('/avocado/predict', methods=['POST'])
def predict():
    """
    Endpoint for avocado price prediction.
    Expected JSON input format:
    {
        "Quality1": float,
        "Quality2": float,
        "Quality3": float,
        "Small Bags": float,
        "Large Bags": float,
        "XLarge Bags": float,
        "year": int,
        "type": string,
        "region": string
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        is_valid, error_message = validate_input(data)
        if not is_valid:
            return jsonify({
                'error': 'Invalid input',
                'message': error_message
            }), 400
            
        # Preprocess input
        input_df = preprocess_input(data)
        
        # Make prediction
        prediction = pipeline.predict(input_df)
        
        # Convert prediction to Python float and round to 2 decimals
        predicted_price = float(round(prediction[0], 2))
        
        return jsonify({
            'predicted_price': predicted_price
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Prediction error',
            'message': str(e)
        }), 500

# Error handler for invalid JSON
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'error': 'Bad request',
        'message': 'Invalid JSON format in request body'
    }), 400

if __name__ == '__main__':
    app.run(debug=True)
