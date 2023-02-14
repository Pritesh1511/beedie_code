import pandas as pd
import streamlit as st

st.write("APP WORKING")
tickers = ['AAPL','DIS','IBM']
st.selectbox("Pick a ticker",tickers)
df = pd.read_csv(tickers+".csv",parse_dates=['Date'],index_col=['Date'])

st.write(df)
