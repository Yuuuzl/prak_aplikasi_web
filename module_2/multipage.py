# MULTIPAGE APPS dengan fungsi

import streamlit as st

def main_page():
    st.markdown("# Main Page")
    st.sidebar.markdown("## Main Page Sidebar") 
    
def page_2():
    st.markdown("# Second Page")
    st.sidebar.markdown("## Second Page Sidebar")
    
def page_3():
    st.markdown("# Third Page")
    st.sidebar.markdown("## Third Page Sidebar")    
    
page_names_to_function = {
    "Main Page": main_page,
    "Second Page": page_2,
    "Third Page": page_3 
}

selected_page = st.sidebar.selectbox("Go to", list(page_names_to_function.keys()))
page_names_to_function[selected_page]()

