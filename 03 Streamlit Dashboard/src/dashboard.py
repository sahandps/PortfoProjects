import streamlit as st
from password_generator import PasswordGenerator, PinCodeGenerator,RandomPasswordGenerator , MemorablePasswordGenerator



st.title("Password Generator")

option = st.radio(
    "Select a password Generator",
    ("Random Password", "Memorable Password", "Pin Code")
)


if option == "Pin Code":
    length = st.slider("Select the lenght of the pin code", 4 , 32)
    generator = PinCodeGenerator(length)
elif option == "Random Password":
    length = st.slider("Select the lenght of the Password", 8 , 32)
    include_symbol = st.toggle("Include Symbols")
    include_number = st.toggle("Include Number")
    generator = RandomPasswordGenerator(length, include_number, include_symbol)
elif option == "Memorable Password":
    length = st.slider("Select Number of words", 4 , 10)
    Separator = st.text_input("Seperator", value="-")
    capitalization = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(length, Separator, capitalization)


password = generator.generate()
st.write(f"Your password is: `{password}` ")