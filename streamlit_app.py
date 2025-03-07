# streamlit_app.py
# 
# import streamlit as st
# import pandas as pd
# from streamlit_gsheets import GSheetsConnection
# 
# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)
# 
# df = conn.read(
#     worksheet="portfolio.xlsx",
#     ttl="10m",
#     usecols=[0, 1],
#     nrows=3,
# )
# 
# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")
# In this example, we are reading a Google Sheets file named portfolio.xlsx and displaying the first three rows of columns 0 and 1. The ttl parameter sets the time-to-live (TTL) for the cache, which is set to 10 minutes in this case. The usecols parameter specifies the columns to be read. We are using it to read only the first two columns. The nrows parameter specifies the number of rows to be read. We are reading the first three rows in this example.
# 
# The itertuples() method is used to iterate over the rows of the DataFrame. The row variable is an object that contains the values of each row. We are using it to display the name and pet of each person in the DataFrame.

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(    worksheet="portfolio.xlsx",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")