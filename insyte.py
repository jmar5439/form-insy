import streamlit as st

def main():
    st.title("Construction Project Information")

    submitted_project_details = []  # List to store submitted project details
    submitted_construction_details = []  # List to store submitted construction details
    
    with st.form("Project Details"):
        st.header("Project Details")
        gemeinde = st.text_input("Gemeinde")
        subcontractor = st.text_input("Subcontractor")
        subco_representative = st.text_input("SubCo Representative")
        submit_button_project = st.form_submit_button("Submit Project Details")
    
    st.header("Construction Details")
    
    col1, col2, col3, col4, col5, col6= st.columns(6)
    
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
        section = st.text_input("Drilling")

    with col6:
        st.subheader("Historic")
        section = st.text_input("Historic")
    
    submit_button = st.button("Submit Construction Details")

    if submit_button_project:
        # Store project details
        submitted_project_details.append(("Gemeinde", gemeinde))
        submitted_project_details.append(("Subcontractor", subcontractor))
        submitted_project_details.append(("SubCo Representative", subco_representative))
    
    if submit_button:
        # Store construction details
        submitted_construction_details.append(("Section", section))
        submitted_construction_details.append(("Length (m)", length))
        submitted_construction_details.append(("Surface Type", surface_type))
        submitted_construction_details.append(("Trench Size (cm)", trench_size))

    # Display submitted project details
    if submitted_project_details:
        st.header("Submitted Project Details")
        for detail in submitted_project_details:
            st.write(f"- {detail[0]}: {detail[1]}")
    
    # Display submitted construction details
    if submitted_construction_details:
        st.header("Submitted Construction Details")
        for detail in submitted_construction_details:
            st.write(f"- {detail[0]}: {detail[1]}")

if __name__ == "__main__":
    main()
