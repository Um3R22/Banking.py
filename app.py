import json
import streamlit as st# 
from read_file import read_file


file_path='users.Json'
data= read_file (file_path)
st.ta ('show data')

st.sidebar.title('Side Bar')
st.write("data")
st.write (data)
