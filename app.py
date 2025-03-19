# Import required libraries
import streamlit as st
import string
import random
import time
import re

st.set_page_config(page_title="Password Generate & Check",layout="centered")

# Function to generate a random password based on user preferences
# Parameters:
#   length: Integer - desired length of password
#   use_uppercase: Boolean - include uppercase letters
#   use_lowercase: Boolean - include lowercase letters
#   use_digits: Boolean - include numbers
#   use_special: Boolean - include special characters
def generate_password(length,use_uppercase,use_lowercase,use_digits,use_special):
    # Start with lowercase letters as base character set
    character = string.ascii_lowercase  

    # Add additional character sets based on user preferences
    if use_uppercase:
        character += string.ascii_uppercase               
    if use_lowercase:
        character += string.ascii_lowercase
    if use_digits:
        character += string.digits  
    if use_special:
        character += string.punctuation

    # Generate and return random password using selected character sets
    password = ''.join(random.choice(character) for i in range(length)) 
    return password

# Function to evaluate password strength and provide improvement suggestions
# Returns: tuple (strength rating, list of suggestions)
def check_pass_str(password):
    strength = "week"
    suggestion = []

    # Check minimum length requirement
    if len(password) < 6:
        suggestion.append("increase a password lenght (at least 6 characters)")

    # Verify presence of different character types
    if not any(char.isupper() for char in password):
        suggestion.append("Add at least one uppercase character")

    if not any(char.islower() for char in password):
        suggestion.append("Add at least one lowercase character")
    
    if not any(char.isdigit() for char in password):
        suggestion.append("Add at least one number character")

    # Check for special characters using regex
    if not re.search(r"[@#$%^&*!]", password):
        suggestion.append("Add at least one special character")
    
    # Determine password strength based on length and number of missing criteria
    if len(password) >= 8 and len(suggestion) <= 1:
        strength = "strong"
    if len(password) >= 6 and len(suggestion) <= 2:
        strength = "Medium"

    return strength, suggestion

# streamlit UI 
#        """Password Generator App"""

st.markdown("## 🔑Password Generator & Strength Meter")
st.markdown("""<span style='font-size:20px;'><span style='color:aqua;'>Welcome!</span> 
            to Password Generator & Strength Meter</span>""",unsafe_allow_html=True)
st.write("This app generates a random password based on the user's choice of character sets and checks the strength of the password.")
st.divider()
st.subheader("Password Generator")
st.write("It generates a random password based on the user's choice of character sets.")

# Add a slider for the user to select the password length
length=st.slider("Select the length for generating a password: ",min_value=8,max_value=32,value=10)

st.write("We are highly recommand to check all boxes if you need a secure password!")

# checkbokes for the user to select the character sets
use_uppercase= st.checkbox("Use Uppercase")
use_lowercase= st.checkbox("Use Lowercase")
use_digits= st.checkbox("Use Digits")
use_special= st.checkbox("Use Special Characters")

# generated password
password_gen = generate_password(length,use_uppercase,use_lowercase,use_digits,use_special)

# add a button generate the password
if st.button("Generate"):
    # spinner loading show when user click on generate and password is generating
   with  st.spinner("Generating Password..."):
         time.sleep(4)
         st.write("##### Generated Password is :")
         st.success(f"{password_gen}")

#       """Password strength meter """
st.divider()
st.subheader("Password Strength Meter") 
st.markdown(" It checks the strength of the password & It also provide suggestions to improve the password strength.")

# user input
password = st.text_input("Enter Your Password:")

if st.button("check strength"):
 with st.spinner("checking..",show_time=True):
    time.sleep(2)
    
 if password:
    strength , suggestion = check_pass_str(password)
    st.markdown(f"##### Your password : {password}")

    if suggestion:
         st.markdown("#### Suggestions to Improve:")
         for s in suggestion:
             st.write(f"- {s}")
    else:
        st.success("Your password is strong and secure!")
st.divider()
st.markdown("<div style='font-weight:bold; text-align:center; font-style:italic;'>Developed by <span style='color:#3dd17ce0;'>Hammad Iqbal</span></div>",unsafe_allow_html=True)