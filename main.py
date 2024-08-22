import streamlit as st
import pandas as pd

st.title("Simple Streamlit App")

# Upload a file
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        # Check file extension
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("File uploaded successfully!")
        st.dataframe(df)
    except Exception as e:
        st.write(f"Error loading file: {e}")
else:
    st.write("Please upload a CSV or Excel file.")
