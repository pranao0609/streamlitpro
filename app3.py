import streamlit as st

def main():
    st.title("Simple Login and Registration Page")

    menu = ["Home", "Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the Home Page")
        st.write("Please use the sidebar to navigate to the login or registration page.")

    elif choice == "Login":
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            st.info(f"Attempted login with username: {username} and password: {password}")
            st.success(f"Welcome {username}!") 

    elif choice == "Register":
        st.subheader("Create a New Account")

        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        if st.button("Register"):
            st.info(f"Attempted registration with username: {new_username} and password: {new_password}")
            st.success("Account created successfully!")
            st.info("Go to the Login page to log in")

if __name__ == '__main__':
    main()