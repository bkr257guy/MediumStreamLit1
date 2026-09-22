import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

#From requirements.txt (I think this is what we imported above) st-gsheets-connection

st.title("Database Entry Categorizer")

# 1. Establish a free secure connection to a Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(ttl=0)

# Ensure we track which item we are currently sorting using session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Find rows that haven't been categorized yet
pending_df = df[(df['Category'].isna()) | (df['Category'] == "none")]

if not pending_df.empty:
    # Get the first unsorted entry
    current_row = pending_df.iloc[0]
    row_id = current_row.name # Get row index to update it later
    
    st.write("### Current Entry to Sort:")
    st.info(f"**Item:** {current_row['Item_Name']}")
    st.write(f"Description: {current_row['Description']}")

    # 2. Display the 3 sorting buttons side-by-side
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📁 Category A"):
            df.at[row_id, 'Category'] = 'Category A'
            conn.update(data=df)
            st.rerun()
            
    with col2:
        if st.button("📁 Category B"):
            df.at[row_id, 'Category'] = 'Category B'
            conn.update(data=df)
            st.rerun()
            
    with col3:
        if st.button("📁 Category C"):
            df.at[row_id, 'Category'] = 'Category C'
            conn.update(data=df)
            st.rerun()
else:
    st.success("🎉 All entries have been sorted!")