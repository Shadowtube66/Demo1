
#imports

import streamlit as st
import plotly.express as px
import seaborn as sns
import numpy as np

#loading datasets

tips = sns.load_dataset('tips')
hp = sns.load_dataset('healthexp')

#Plots

fig1 = px.bar(tips,x="sex",y="alive")
fig2 = px.scatter(tips,x="sex",y="tip")

# Streamlit web app layout
st.title("Data Visualization with Plotly")

# Section 1: Bar Plot

st.header("Plot 1: Bar Plot - Gender by Alive")
st.plotly_chart(fig1)
st.markdown('''**Insight Observed**: (More females survived than males during the titanic)''')

# Section 2: Violin Plot

st.header("Plot 2: Violin Plot - Gender by Tips")
st.plotly_chart(fig2)
st.markdown('''**Insight Observed**: (Majority tips lie within the range of 2 to 4)''')