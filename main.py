import streamlit as st
import pandas as pd

# Load the CSV dataset
df = pd.read_csv("genders.csv")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f5;
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #4a4e69;
        text-align: center;
    }
    .stSelectbox, .stTextInput {
        margin-bottom: 20px;
    }
    .name {
        font-size: 18px;
        color: #22223b;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app layout
st.title("Nepali People Name Generator")

# Gender selection (default: male)
gender = st.selectbox("Select Gender:", options=["male", "female"], index=0)

# First letter selection using a dropdown list from A to Z (default: A)
first_letter = st.selectbox("Select the first letter of the name:", options=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), index=0)

# Button to generate names
if st.button("Generate Names") and gender and first_letter:
    # Filter the dataframe based on gender and first letter
    filtered_names = df[(df['gender'] == gender) & (df['name'].str.startswith(first_letter.lower()))]
    
    # Check if there are names available
    if not filtered_names.empty:
        # Get random names based on count
        name_samples = filtered_names.sample(min(5, len(filtered_names)), replace=False)
        st.write("Generated Names:")
        for index, row in name_samples.iterrows():
            st.write(f"<div class='name'>{row['name'].capitalize()}</div>", unsafe_allow_html=True)
    else:
        st.error("Sorry, no names available for the selected criteria.")
else:
    st.info("Please select both gender and the first letter.")

# Button to generate more names
if st.button("Generate More") and gender and first_letter:
    # Filter the dataframe again and generate more names
    filtered_names = df[(df['gender'] == gender) & (df['name'].str.startswith(first_letter.lower()))]
    
    if not filtered_names.empty:
        name_samples = filtered_names.sample(min(5, len(filtered_names)), replace=False)
        st.write("Generated Names:")
        for index, row in name_samples.iterrows():
            st.write(f"<div class='name'>{row['name'].capitalize()}</div>", unsafe_allow_html=True)
    else:
        st.error("Sorry, no names available for the selected criteria.")
