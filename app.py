import streamlit as st
import pandas as pd
import os

# CSV file to store student data
DATA_FILE = "students.csv"

# Initialize CSV file if not exists
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Roll No", "Department"])
    df.to_csv(DATA_FILE, index=False)

st.title("🎓 Student Registration System")

menu = st.sidebar.selectbox("Menu", ["Register Student", "View Students"])

if menu == "Register Student":
    st.header("Register New Student")
    name = st.text_input("Enter Student Name")
    roll = st.text_input("Enter Roll Number")
    dept = st.text_input("Enter Department")

    if st.button("Submit"):
        if name and roll and dept:
            df = pd.read_csv(DATA_FILE)
            new_data = {"Name": name, "Roll No": roll, "Department": dept}
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success(f"Student '{name}' registered successfully!")
        else:
            st.error("Please fill all fields!")

elif menu == "View Students":
    st.header("Registered Students")
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        st.info("No students registered yet.")
    else:
        st.dataframe(df)
