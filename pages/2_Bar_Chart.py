import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt #ignore warning


st.title('Bar Chart')


df = pd.read_csv('data/dataset_ok.csv')

if st.checkbox('Show data',key='1'):
    st.write(df) 


gender = df['Gender'].unique()
# st.write(gender)




selected_gender= st.selectbox("Select Gender",options=gender,index=0)

df_amount_category_gender = df.groupby(['Product Category','Gender'])['Purchase Amount'].sum().unstack()

if st.checkbox('Show data in bar chart',key='2'):
    st.write(df_amount_category_gender)

x = np.arange(len(df_amount_category_gender.index))

colors = st.color_picker("Pick A Color", "#00f900")

plt.figure(figsize=(12,6))
gender_data = df_amount_category_gender[selected_gender]
x = np.arange(len(gender_data.index))

plt.bar(x, gender_data, width=0.5, label=selected_gender,color=colors,alpha=0.7)



plt.title('Total Purchase Amount by Product Category and Gender')
plt.ylabel('Total Purchase Amount')
plt.xlabel('Product Category')
plt.xticks(x, df_amount_category_gender.index)
plt.grid()

st.pyplot(plt)
