import streamlit as st
import requests
import json

# Set page config
st.set_page_config(
    page_title="🥑 Avocado Price Predictor",
    page_icon="🥑",
    layout="centered"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🥑 Avocado Price Predictor")
st.markdown("""
    Welcome to the Avocado Price Predictor! Enter your avocado details below to get a price prediction.
    Our ML model will analyze the data and provide an estimated price. 
    """)

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    # Quality measures
    st.subheader("Quality Metrics")
    quality1 = st.number_input(
        "Quality1",
        min_value=0.0,
        help="Example: 1036.74",
        placeholder="Enter Quality1 value"
    )
    
    quality2 = st.number_input(
        "Quality2",
        min_value=0.0,
        help="Example: 54454.85",
        placeholder="Enter Quality2 value"
    )
    
    quality3 = st.number_input(
        "Quality3",
        min_value=0.0,
        help="Example: 48.16",
        placeholder="Enter Quality3 value"
    )

with col2:
    # Bag sizes
    st.subheader("Bag Quantities")
    small_bags = st.number_input(
        "Small Bags",
        min_value=0.0,
        help="Example: 8603.62",
        placeholder="Enter small bags quantity"
    )
    
    large_bags = st.number_input(
        "Large Bags",
        min_value=0.0,
        help="Example: 93.25",
        placeholder="Enter large bags quantity"
    )
    
    xlarge_bags = st.number_input(
        "XLarge Bags",
        min_value=0.0,
        help="Example: 0.0",
        placeholder="Enter extra large bags quantity"
    )

# Additional information
st.subheader("Additional Information")
col3, col4 = st.columns(2)

with col3:
    year = st.number_input(
        "Year",
        min_value=2000,
        max_value=2025,
        value=2015,
        help="Example: 2015",
        placeholder="Enter year"
    )

with col4:
    avocado_type = st.selectbox(
        "Type",
        options=["conventional", "organic"],
        help="Select avocado type"
    )

region = st.selectbox(
    "Region",
    options=["Albany", "Atlanta", "BaltimoreWashington", "Boise", "Boston",
             "BuffaloRochester", "California", "Charlotte", "Chicago",
             "Cincinnati", "Columbus", "DallasFtWorth", "Denver", "Detroit",
             "GrandRapids", "GreatLakes", "HarrisburgScranton", "HartfordSpringfield",
             "Houston", "Indianapolis", "Jacksonville", "LasVegas", "LosAngeles",
             "Louisville", "MiamiFtLauderdale", "Midsouth", "Nashville", "NewOrleansMobile",
             "NewYork", "Northeast", "NorthernNewEngland", "Orlando", "Philadelphia",
             "PhoenixTucson", "Pittsburgh", "Plains", "Portland", "RaleighGreensboro",
             "RichmondNorfolk", "Roanoke", "Sacramento", "SanDiego", "SanFrancisco",
             "Seattle", "SouthCarolina", "SouthCentral", "Southeast", "Spokane",
             "StLouis", "Syracuse", "Tampa", "TotalUS", "West", "WestTexNewMexico"],
    help="Select region"
)

# Prediction button and result display
if st.button("🔮 Predict Price"):
    # Prepare the data
    data = {
        "Quality1": quality1,
        "Quality2": quality2,
        "Quality3": quality3,
        "Small Bags": small_bags,
        "Large Bags": large_bags,
        "XLarge Bags": xlarge_bags,
        "year": year,
        "type": avocado_type,
        "region": region
    }
    
    try:
        # Make prediction request
        response = requests.post(
            "http://localhost:5000/avocado/predict",
            json=data
        )
        
        if response.status_code == 200:
            prediction = response.json()["predicted_price"]
            st.success(f"💰 Predicted Price: ${prediction:.2f}")
        else:
            st.error(f"Error: {response.json()['message']}")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the prediction service. Please make sure the Flask backend is running.")

# Footer
st.markdown("---")
st.markdown("Made with 🥑 by Your Friendly AI Assistant")