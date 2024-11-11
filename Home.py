import streamlit as st
import pandas as pd
st.title("Welcome to my Streamlit app")


st.header("About Dataset")

st.write(
"""This dataset contains transaction details of users, including their demographics and purchasing behavior. It features information such as User ID, Age, Gender, Country, Purchase Amount, Purchase Date, and Product Category. This data can be useful for analyzing consumer trends, demographic influences on purchasing behavior, and market segmentation.

    - User ID: A unique identifier assigned to each user for tracking their transactions.
    - Age: The age of the user at the time of purchase, which may influence buying behavior.
    - Gender: The gender of the user, allowing for demographic segmentation of purchasing patterns.
    - Country: The country of residence for the user, useful for regional market analysis.
    - Purchase Amount: The total amount spent by the user during a transaction.
    - Purchase Date: The date when the purchase was made, allowing for temporal analysis of buying behavior.
    - Product Category: The category of the product purchased, aiding in understanding consumer preferences.
""")

    


df = pd.read_csv('data/dataset_ok.csv')

st.dataframe(df)

st.markdown("Source data: [Kaggle](https://www.kaggle.com/datasets/refiaozturk/online-shopping-dataset)")
st.markdown("Source code: [Github](https://github.com/vanhhoang1812/streamlit.git)")
st.markdown("Streamlit Web App: [Streamlit](https://demo-app-vanh.streamlit.app/)")


st.markdown(""" Follow me: 
[Github](https://github.com/VanhHoang),
[Facebook](https://www.facebook.com/vanh.hoang.7359/) and
[Kaggle](https://www.kaggle.com/vanhhong)
""")
