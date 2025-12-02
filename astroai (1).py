import google.generativeai as genai
import streamlit as st
import datetime

st.title("🔮Welcome to Astro AI🌟")
st.subheader("*Your cosmic companion for exploring the universe through the power of Ai...*")
##
genai.configure(api_key=st.secrets["Api_Key"])
model = genai.GenerativeModel("gemini-2.5-flash")

###
name= st.text_input("Enter Your Name:")
dob = st.date_input("Enter Your Date Of Birth(YYYY/MM/DD):",min_value =datetime.date (1000,1,1))
birth_location= st.text_input("Enter Your Birth Location:")
birth_time = st.text_input("Enter Your Birth Time(HH:MM):")
if name and dob and birth_location and birth_time:
    st.success(f"Hello ***{name}***! Ready to explore the universe with Astro AI?")
    prompt= (f"Act like a Give an astrological-style suggestion for {name},"
        f"born on {dob} at {birth_time} in {birth_location}."
        "Make it friendly, inspiring, and easy to understand."
    )
    response=model.generate_content(prompt)
    st.info(response.text)
else:
    st.warning("Please enter your details.")

