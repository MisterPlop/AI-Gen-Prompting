# 🥑 Avocado Price Prediction Project

This project predicts avocado prices using machine learning. It consists of three main components:
- Jupyter notebook for model training and export
- Flask API backend for predictions
- Streamlit frontend for user interaction

## 📊 Project Structure
```
.
├── model_training.ipynb
├── app.py
├── frontend.py
├── avocado_price_predictor.pkl
├── requirements.txt
└── README.md
```

## 🛠️ Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

> 📝 To generate requirements.txt (for contributors):
> ```bash
> pip freeze > requirements.txt
> ```

## 📦 Requirements

Main dependencies:
- pandas
- numpy
- scikit-learn
- xgboost
- flask
- streamlit
- joblib

Full list in `requirements.txt`

## 🚀 Running the Project

### 1. Model Training (Optional - PKL file provided)
```bash
jupyter notebook model/model_training.ipynb
```
- Opens notebook for model training
- Uses `avocado.csv` dataset
- Exports trained model as `avocado_price_predictor.pkl`

### 2. Start Flask Backend
```bash
python app.py
```
- Runs on `http://localhost:5000`
- Endpoint: `/avocado/predict` (POST)

### 3. Launch Streamlit Frontend
```bash
streamlit run frontend.py
```
- Opens automatically in browser
- Usually on `http://localhost:8501`

## 🎯 Usage Example

### API Direct Call
```python
import requests

data = {
    "Quality1": 1036.74,
    "Quality2": 54454.85,
    "Quality3": 48.16,
    "Small Bags": 8603.62,
    "Large Bags": 93.25,
    "XLarge Bags": 0.0,
    "year": 2015,
    "type": "conventional",
    "region": "Albany"
}

response = requests.post("http://localhost:5000/avocado/predict", json=data)
print(f"Predicted price: ${response.json()['predicted_price']:.2f}")
```

### Frontend
1. Open the Streamlit app
2. Fill in the form with avocado details
3. Click "Predict Price"
4. Get instant price prediction

## ⚠️ Important Notes
- Ensure Flask backend is running before starting Streamlit
- Model expects specific regions and avocado types
- All numeric inputs must be positive
- Price predictions are in USD

## 🔍 Model Details
- Uses XGBoost Regressor
- Features both numerical and categorical data
- Trained on historical avocado prices
- Includes data preprocessing pipeline

## 👥 Contributing
To contribute:
1. Fork the repository
2. Create a feature branch
3. Update requirements.txt if needed
4. Submit a pull request

## 📝 License
MIT License

---
Created with 🥑 by Claude & Alan (Yours to guess who's the AI assistant!)
