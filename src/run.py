import streamlit as st
st.title("TODO")
st.segmented_control("what's to do?", ["add" , "all", "today", "complete" , "delete"])

if st.segmented_control("what's to do?") == "add":
    st.text_input("work")
    st.text_input("description")
    st.text_input("time")
    st.date_input("date")
    st.form_submit_button("submit")








