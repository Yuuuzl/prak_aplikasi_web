import streamlit as st
import time

# Fungsi yang lambat untuk melakukan operasi, hasilnya di-cache
@st.cache_data(persist=True)
def my_slow_function(angka1, angka2):
    # Simulasi operasi yang sangat lambat
    time.sleep(3)
    return angka1 + angka2


#Contoh penggunaan fungsi di atas
st.title("Caching Example with Streamlit")

# Input user
angka1 = st.number_input("Enter first number:", value=0)
angka2 = st.number_input("Enter second number:", value=0)

#Tombol untuk menjalankan fungsi lambat
if st.button("Calculate Sum"):
    result = my_slow_function(angka1, angka2)
    st.write(f"The result is: {result}")


