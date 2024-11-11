import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime as dt

st.title('Line Chart')

df = pd.read_csv('data/dataset_ok.csv')


if st.checkbox('Show data',key='1'):
    st.subheader('Data')
    st.write(df)

#Chuyển dữ liệu cột Purchase Date sang dạng date
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
df["Year"] = df["Purchase Date"].dt.year
# st.write(df)


category = df["Product Category"].unique().tolist()
selected_category = st.multiselect('Select Category', options=category,default=category[0])

df_amount_category_date = df.groupby(['YearMonth','Product Category'])['Purchase Amount'].sum().unstack()

if st.checkbox('Show data in bar chart',key='2'):
    st.write(df_amount_category_date)

plt.figure(figsize=(15,10))


for category in selected_category:
    category = df_amount_category_date[category]
    # st.write(category)
    plt.title('Purchase Amount by Category')
    plt.legend(selected_category)
    plt.xlabel('YearMonth')
    plt.ylabel('Purchase Amount')
    plt.xticks(rotation=90)
    plt.plot(category.index,category.values,marker='o')

import streamlit as st

colors = st.select_slider(
    "Select a color fill",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)


if st.checkbox('Grid',key="3"):
    plt.grid()
if st.checkbox('Fill area',key="4"):
    plt.fill_between(category.index,category.values,alpha=0.3,color=colors)  

plt.title('Purchase Amount by Category')
plt.legend(selected_category)
plt.xlabel('YearMonth')
plt.ylabel('Purchase Amount')
plt.xticks(rotation=90)

st.pyplot(plt)
