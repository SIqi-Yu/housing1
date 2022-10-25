import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Lucy Yu')
df = pd.read_csv('housing.csv')

value_filter = st.slider('Minimal Median House Price',0,500001,10)

df = df[df.median_house_value >= value_filter]

location_filter = st.sidebar.multiselect(
    'choose the location type',
    df.ocean_proximity.unique(), 
    df.ocean_proximity.unique()
)


# a radio button
income_genre = st.radio(
    "Choose the income level",
    ('Low','Median','High'))

if income_genre == 'Low':
    df = df[df.median_income <= 2.5]
elif income_genre == 'Median':
    df = df[df.median_income > 2.5 & df.median_income < 4.5]
else:
    df = df[df.median_income >= 4.5]

# filter by proximity
df = df[df.ocean_proximity.isin(location_filter)]

st.subheader('see more filter on the sidebar')

st.map(df)

# display of histogram
st.subheader('Histogram of the Median House Price')
fig, ax = plt.subplots(figsize=(20,5))
df.median_income.hist(bins=30)
st.pyplot(fig)