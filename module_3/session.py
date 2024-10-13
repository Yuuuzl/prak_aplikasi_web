import streamlit as st

if 'key' not in st.session_state:
    st.error("You are not logged in!")

try:
    st.write(f"The value of 'key' is'{st.session_state}'")

    if st.button("Log out"):
        del st.session_state.key
        st.rerun()

except Exception as e:
    st.write(f"The value of 'key' is unidentified")
    if st.button("Log in", key="key"):
        st.session_state.key = 'value'
        st.rerun() 