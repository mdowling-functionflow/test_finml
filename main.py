import numpy as np
import pandas as pd
import streamlit as st

st.write("""
My first stock app
Hello *world*!
""")

df=pd.read_csv('./data/tsla_onemonth.csv')

st.write(df)

st.line_chart(df)
