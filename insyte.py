import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('construction_data.db')
c = conn.cursor()

# Create a table for submitted data if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS construction_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              detail_category TEXT,
              detail_value TEXT)''')
conn.commit()

def insert_data(detail_category, detail_value):
    # Insert submitted data into the database
    c.execute("INSERT INTO construction_data (detail_category, detail_value) VALUES (?, ?)", (detail_category, detail_value))
    conn.commit()

def fetch_submitted_data():
    # Fetch the submitted data from the database
    c.execute("SELECT * FROM construction_data")
    submitted_data = c.fetchall()
    return submitted_data

def main():
    st.title("Construction Project Information")

    with st.form("Project Details"):
        st.header("Project Details")
        gemeinde = st.text_input("Gemeinde")
        subcontractor = st.text_input("Subcontractor")
        subco_representative = st.text_input("SubCo Representative")
        submit_button_project = st.form_submit_button("Submit Project Details")
    
    st.header("Construction Details")
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.subheader("Section")
        section = st.text_input("Section")
    
    with col2:
        st.subheader("Length (m)")
        length = st.number_input("Length (m)", min_value=0.0)
    
    with col3:
        st.subheader("Surface Type")
        surface_types = ["Asphalt", "Brick", "Grass"]
        surface_type = st.selectbox("Surface Type", surface_types)
    
    with col4:
        st.subheader("Trench Size (cm)")
        trench_sizes = ["15x45", "30x60", "30x80"]
        trench_size = st.selectbox("Trench Size (cm)", trench_sizes)

    with col5:
        st.subheader("Drilling")
        drilling = st.text_input("Drilling")

    with col6:
        st.subheader("Historic")
        historic = st.text_input("Historic")
    
    submit_button = st.button("Submit Construction Details")

    if submit_button_project:
        # Store project details in the database
        insert_data("Gemeinde", gemeinde)
        insert_data("Subcontractor", subcontractor)
        insert_data("SubCo Representative", subco_representative)
    
    if submit_button:
        # Store construction details in the database
        insert_data("Section", section)
        insert_data("Length (m)", length)
        insert_data("Surface Type", surface_type)
        insert_data("Trench Size (cm)", trench_size)
        insert_data("Drilling", drilling)
        insert_data("Historic", historic)

    # Fetch and display submitted data from the database in a table
    submitted_data = fetch_submitted_data()
    if submitted_data:
        st.header("Submitted Details")
        headers = ["Section", "Length (m)", "Surface Type", "Trench Size (cm)", "Drilling", "Historic"]
        values = [data[2] for data in submitted_data if data[1] in headers]
        data_dict = {header: value for header, value in zip(headers, values)}
        st.write(pd.DataFrame([data_dict]))

if __name__ == "__main__":
    main()
