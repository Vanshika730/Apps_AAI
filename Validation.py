import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime
 
# Function to load existing user data
def load_user_data(email):
    file_path = f'users/{email}.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return None
 
# Function to save new user data
def save_user_data(data):
    email = data['email']
    user_folder = 'users'
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    file_path = f'{user_folder}/{email}.json'
    with open(file_path, 'w') as file:
        json.dump(data, file)
 
# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Login", "Sign Up"])
 
if page == "Sign Up":
    st.title("Welcome to the Sign-Up Page")
    # Input fields for Sign-Up form
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    dob = st.date_input("DOB")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        # Check if user already exists
        if load_user_data(email):
            st.warning("A user with this email already exists. Please log in.")
        else:
            # Create user data and save it
            user_data = {
                "name": name,
                "phone": phone,
                "dob": dob.strftime('%Y-%m-%d'),
                "email": email,
                "password": password
            }
            save_user_data(user_data)
            st.success("Sign Up successful! You can now log in.")
elif page == "Login":
    st.title("Welcome to the Login Page")
    # Input fields for login
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Load user data
        user_data = load_user_data(email)
        if user_data:
            # Validate password
            if user_data['password'] == password:
                st.success(f"Welcome, {user_data['name']}!")
                # Display user info
                st.write("### User Information")
                st.write(f"**Name:** {user_data['name']}")
                st.write(f"**Phone:** {user_data['phone']}")
                st.write(f"**Date of Birth:** {user_data['dob']}")
                # Allow the user to proceed to marks entry
                if st.button("Proceed to Marks Entry"):
                    # This is where the marks entry page would go
                    st.write("Marks entry page (to be implemented).")
            else:
                st.error("Incorrect password.")
        else:
            st.error("User does not exist. Please sign up first.")
