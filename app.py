import streamlit as st

st.title("🧠 Mental Health AI")

hr = st.number_input("Heart Rate")
sleep = st.number_input("Sleep Hours")
screen = st.number_input("Screen Time")

if st.button("Analyze"):
    if hr > 100 and sleep < 5:
        st.error("High Stress ⚠️")
    else:
        st.success("Normal 😊")
